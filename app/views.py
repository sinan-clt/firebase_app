from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status
import requests
import json
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.permissions import BasePermission, IsAuthenticated, AllowAny
from rest_framework.response import Response



class SendPushNotitification(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        # Replace 'YOUR_SERVER_KEY' with your Firebase Server Key
        server_key = 'YOUR SERVER KEY'

        # Get the device token, title, and body from the request data
        device_token = request.data.get('device_token')
        title = request.data.get('title', 'New Notification')
        body = request.data.get('body', 'Hello from Django API!')

        if not device_token:
            return Response({'message': 'Device token is missing'}, status=status.HTTP_400_BAD_REQUEST)


        # Set up the data payload for the notification
        data = {
            'notification': {
                'title': title,
                'body': body,
            },
            'to': device_token,
        }

        # Send the request to Firebase Cloud Messaging API
        headers = {
            'Authorization': f'key={server_key}',
            'Content-Type': 'application/json',
        }
        response = requests.post('https://fcm.googleapis.com/fcm/send', json=data, headers=headers)

        # Check the response and return a DRF Response
        if response.status_code == 200:
            return Response({'message': 'Notification sent successfully'})
        else:
            return Response({'message': 'Failed to send notification'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
