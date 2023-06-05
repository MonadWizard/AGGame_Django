from channels.generic.websocket import AsyncWebsocketConsumer
import json
from auth_user_app.models import User
from asgiref.sync import sync_to_async

from django.contrib.auth import get_user_model


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




class SportsScoreConsumerAuth(AsyncWebsocketConsumer):
    async def connect(self):

        # self.connect_user = self.scope["url_route"]["kwargs"]["userid"]
        headers = dict(self.scope["headers"])
        print("headers : ", headers)
        print(f"\n\nToken: {headers[b'authorization'].decode('utf-8')}\n\n")

        # headers :  {b'host': b'aggapi.algorithmgeneration.com', b'x-real-ip': b'162.158.207.155', b'x-forwarded-for': b'103.19.131.77, 162.158.207.155', b'x-forwarded-proto': b'https', b'upgrade': b'websocket', b'connection': b'upgrade', b'accept-encoding': b'gzip', b'cf-ray': b'7d275c85dc8e78c7-CGP', b'cf-visitor': b'{"scheme":"https"}', b'user-agent': b'Dart/2.19 (dart:io)', b'cache-control': b'no-cache', b'sec-websocket-version': b'13', b'sec-websocket-extensions': b'permessage-deflate; client_max_window_bits', b'sec-websocket-key': b'sIOQ4m0te7rrA6vWhapcfg==', b'cdn-loop': b'cloudflare', b'cf-connecting-ip': b'103.19.131.77', b'cf-ipcountry': b'BD'}
        # headers :  {b'host': b'aggapi.algorithmgeneration.com', b'x-real-ip': b'162.158.207.155', b'x-forwarded-for': b'103.19.131.77, 162.158.207.155', b'x-forwarded-proto': b'https', b'upgrade': b'websocket', b'connection': b'upgrade', b'accept-encoding': b'gzip', b'cf-ray': b'7d275c46cbda78b7-CGP', b'cf-visitor': b'{"scheme":"https"}', b'sec-websocket-version': b'13', b'sec-websocket-key': b'2wZ+oxchdMqUBKRH3kdOcw==', b'authorization': b'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg2MDMzNTg2LCJpYXQiOjE2ODU5NDY1ODYsImp0aSI6ImQ5MmE4YTNjYzYwYzQ4ODA4MGJhYTU1MTMyNGQ0OTk0IiwidXNlcl9pZCI6IjA2MDQwNTA0NDQyOTU2OTcifQ.L1tF_QY5pf83_O9zotWrfL6wuguvTGE712Tknv0yNfo', b'sec-websocket-extensions': b'permessage-deflate; client_max_window_bits', b'cdn-loop': b'cloudflare', b'cf-connecting-ip': b'103.19.131.77', b'cf-ipcountry': b'BD'}
        if self.scope["user"].is_anonymous:
            print("Anonymous user")
            self.connect_user = None
            # pass
        else:
            user = self.scope["user"]
            print("Authenticated user : ", user)
            self.connect_user = user.userid

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
            # user = await sync_to_async(User.objects.get)(userid=self.connect_user)
        if self.connect_user is None:
            await self.send(text_data=json.dumps({
                        'status': 'Anonymous user'
                    }))
            return
            
            
        
                
        # # Only allow the user who initiated the WebSocket connection to send data
        # if self.connect_user != allowed_users:
        #     return

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






class SportsScoreConsumersync(AsyncWebsocketConsumer):
    async def connect(self):

        # self.connect_user = self.scope["url_route"]["kwargs"]["userid"]

        if self.scope["user"].is_anonymous:
            print("Anonymous user")
            self.connect_user = None

            self.connect_match = self.scope["url_route"]["kwargs"]["matchid"]
            self.room_name = self.connect_match
            self.room_group_name = "live_" + self.room_name

            await self.channel_layer.group_add(
                self.room_group_name, 
                self.channel_name)
            await self.accept()
            
            await self.send(text_data=json.dumps({
                        'status': 'Anonymous user'
                    }))
            # force disconnect
            await self.close()
            return
        

        else:
            user = self.scope["user"]
            print("Authenticated user : ", user)
            self.connect_user = user.userid

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
        score = text_data_json['score']
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







class Backup(AsyncWebsocketConsumer):
    async def connect(self):

        # self.connect_user = self.scope["url_route"]["kwargs"]["userid"]

        if self.scope["user"].is_anonymous:
            print("Anonymous user")
            self.connect_user = None
            # pass
        else:
            user = self.scope["user"]
            print("Authenticated user : ", user)
            self.connect_user = user.userid

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
            # user = await sync_to_async(User.objects.get)(userid=self.connect_user)
            if self.connect_user is not None:
                allowed_users = self.connect_user
            else:
                allowed_users = None
                print("NOT allowed user : ", allowed_users)
                return
            
        except User.DoesNotExist:
            allowed_users = 'Not Scorekeeper'
            print("Not Scorekeeper")
                
        # # Only allow the user who initiated the WebSocket connection to send data
        # if self.connect_user != allowed_users:
        #     return

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


