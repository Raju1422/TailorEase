from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from users.serializers import SignupSerializer

class SignupAPIView(APIView):
    def post(self,request):
        try:
            serializer = SignupSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message":"User Created Successfully"},status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error":str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)