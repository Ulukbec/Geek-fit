from rest_framework.response import Response
from rest_framework import status
from geeksfit.models import Training
from geeksfit.serializers import TrainingSerializer, TrainingValidateSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

class TrainingModelViewSet(ModelViewSet):
    queryset = Training.objects.all()
    serializer_class = TrainingSerializer
    pagination_class = PageNumberPagination
    lookup_field = 'id'

    def create(self, request, *args, **kwargs):
        serializer = TrainingValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        training = Training.objects.create(**serializer.validated_data)
        training.save()
        return Response(data=TrainingSerializer(training).data,
                        status=status.HTTP_201_CREATED)
