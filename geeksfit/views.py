from geeksfit.serializers import *
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView, RetrieveAPIView


class TrainingModelViewSet(ListAPIView):
    queryset = Training.objects.all()
    serializer_class = TrainingSerializer
    pagination_class = PageNumberPagination


class TrainingDetailView(RetrieveAPIView):
    queryset = Training.objects.all()
    serializer_class = TrainingDetailSerializer
    lookup_field = 'id'


class FavoriteTrainingListAPIView(ListAPIView):
    queryset = FavoriteTraining.objects.all()
    serializer_class = FavoriteTrainingSerializer
    lookup_field = 'id'

