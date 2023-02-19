from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import *
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, ListAPIView


# Create your views here.

class PersonalInformAPIView(ListAPIView):
    queryset = PersonalInform
    serializer_class = PersonalInformSerializer


class PersonalInformCreateAPIView(ListCreateAPIView):
    queryset = PersonalInform.objects.all()
    serializers = PersonalInformSerializer

    def create(self, request, *args, **kwargs):
        serializer = PersonalInformValidateSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(data={'error': serializer.errors})

        gmail = serializer.validated_data.get('gmail')
        phone_number = serializer.validated_data.get('phone_number')
        gender = serializer.validated_data.get('gender')
        personal_area = PersonalInform.objects.create(gmail=gmail, phone_number=phone_number, gender=gender)
        personal_area.save()
        return Response(data={'message': 'data received',
                              'personal_area': PersonalInformSerializer(personal_area).data})
