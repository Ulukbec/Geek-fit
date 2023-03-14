from rest_framework.response import Response
from .serializers import *
from .models import *
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class EmailProfileView(RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

    def update(self, request, *args, **kwargs):
        user = self.get_object()
        email = request.data.get('email')
        user.email = email
        user.save(update_fields=['email'])
        serializer = self.get_serializer(user)
        return Response(serializer.data)


class PersonalInformAPIView(ListCreateAPIView):
    queryset = PersonalInform.objects.all()
    serializer_class = PersonalInformSerializer

    def create(self, request, *args, **kwargs):
        serializer = PersonalInformValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        personal_area = PersonalInform.objects.create(**serializer.validated_data)
        personal_area.save()
        return Response(data={'message': 'data received',
                              'personal_area': self.serializer_class(personal_area).data})


class PersonalInformRUAPIView(RetrieveUpdateAPIView):
    queryset = PersonalInform.objects.all()
    serializer_class = PersonalInformSerializer
    lookup_field = 'id'


class MyCardAPIView(ListCreateAPIView):
    queryset = MyCard.objects.all()
    serializer_class = MyCardSerializer

    def create(self, request, *args, **kwargs):
        serializer = MyCardValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        my_card = MyCard.objects.create(**serializer.validated_data)
        my_card.save()
        return Response(data={"message": "data received",
                              'my_card': self.serializer_class(my_card).data})


class MyCardRUAPIView(RetrieveUpdateAPIView):
    queryset = MyCard.objects.all()
    serializer_class = MyCardSerializer
    lookup_field = 'id'
