# from channels.generic.websocket import AsyncWebsocketConsumer
# import json

# class SportsScoreConsumer(AsyncWebsocketConsumer):
#     async def connect(self):

#         self.connect_user = self.scope["url_route"]["kwargs"]["userid"]
#         self.connect_match = self.scope["url_route"]["kwargs"]["matchid"]

#         self.room_name = self.connect_match
#         self.room_group_name = "live_" + self.room_name
#         await self.channel_layer.group_add(
#             self.room_group_name, 
#             self.channel_name)
#         # print(f"\nOn connection: {self.room_group_name}, user: {self.connect_user}, match: {self.connect_match}\n")
#         await self.accept()

#         await self.send(text_data=json.dumps({
#             'success': True,
#             'message': 'Connected'
#         }))

#     async def disconnect(self, close_code):
#         await self.channel_layer.group_discard(
#             "sports_scores",
#             self.channel_name
#         )

#     async def receive(self, text_data):
#         text_data_json = json.loads(text_data)
#         score = text_data_json['score']
#         print(f"\nOn receive: {self.room_group_name}, user: {self.connect_user}, match: {self.connect_match}\n")

#     # Broadcast the score to all users in the group
#         await self.channel_layer.group_send(
#             self.room_group_name,
#             {
#                 'type': 'sports_score',
#                 'success': True,
#                 'score': score
#             }
#         )


#     async def sports_score(self, event):
#         score = event['score']
#         print("sports_score : ", score)


        

#         # Send the score to the user
#         await self.send(text_data=json.dumps({
#             'score': score
#         }))









