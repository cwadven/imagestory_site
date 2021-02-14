from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import async_to_sync
import json

from django.db.models.signals import post_save
from django.dispatch import receiver
from channels.layers import get_channel_layer
from board.models import Commentalertcontent

# 리시버 생성을 할 경우 이용하는 것
@receiver(post_save, sender=Commentalertcontent)
def comment_post(sender, instance, created, **kwargs):
    if created:
        channel_layer=get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            # 특정 groupname을 지점 이 경우 instance의 외래키로 묶여져있는 게시글 묶기
            instance.profile_name.user.username, {
                "type": "share_message",
                "message": instance.content.body,
                "sender": instance.sender_name,
                "board_title" : instance.content.main_post.title,
            }
    )

class ChatConsumer(AsyncWebsocketConsumer):
  	# websocket 연결 시 실행
    async def connect(self):
        # chat/routing.py 에 있는
        # path('ws/test/<str:username>/',consumers.ChatConsumer),
        
        # 사용자 아이디로 접근 (나중에 암호화 해서)
        self.groupname = self.scope['url_route']['kwargs']['username']

        # Join room group
        await self.channel_layer.group_add(
            self.groupname,
            self.channel_name
        )
        await self.accept()

		# websocket 연결 종료 시 실행 
    async def disconnect(self, close_code):
        # Leave room group

        await self.channel_layer.group_discard(
            self.groupname,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to room group
        # {}가 chat_message의 event 매소드이다
        # type으로 함수를 결정해서 해당 메시지를 보내는 형식
        # username = self.scope['user'].username if self.scope['user'].username else str(self.scope['headers'][10][1])[2:7]+ "익명"

        await self.channel_layer.group_send(
            self.groupname, {'type': 'share_message', 'message': message, }
        )

    # 메시지 전송
    async def share_message(self, event):
        message = event['message']
        sender = event['sender']
        board_title = event['board_title']
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'sender': sender,
            'board_title': board_title
        }))