from channels.generic.websocket import AsyncWebsocketConsumer
import json
from auth_user_app.models import User
from asgiref.sync import sync_to_async

class SportsScoreConsumer(AsyncWebsocketConsumer):
    async def connect(self):

        self.connect_user = self.scope["url_route"]["kwargs"]["userid"]
        self.connect_match = self.scope["url_route"]["kwargs"]["matchid"]

        self.room_name = self.connect_match
        self.room_group_name = "live_" + self.room_name

        await self.channel_layer.group_add(
            self.room_group_name, 
            self.channel_name)
        await self.accept()

        # Send a confirmation message to the user
        await self.send(text_data=json.dumps({
            'success': True,
            'message': 'Connected'
        }))

    async def disconnect(self, close_code):
        # Remove the channel from the group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        # Parse the incoming data
        text_data_json = json.loads(text_data)

        # Check if the user is allowed to send data
        try:
            user = await sync_to_async(User.objects.get)(userid=self.connect_user)
            if 'Scorekeeper' in user.user_type_flag:
                allowed_users = self.connect_user
            else:
                allowed_users = None            
        except User.DoesNotExist:
            allowed_users = 'Not Scorekeeper'
                
        # Only allow the user who initiated the WebSocket connection to send data
        if self.connect_user != allowed_users:
            return

        score = text_data_json['score']
        # print(f"\nOn receive: {self.room_group_name}, user: {self.connect_user}, match: {self.connect_match}\n")

        # Broadcast the score to all users in the group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'sports_score',
                'success': True,
                'score': score
            }
        )

    async def sports_score(self, event):
        score = event['score']
        print("sports_score : ", score)

        # Send the score to the user
        await self.send(text_data=json.dumps({
            'score': score
        }))
