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

    def get(self, request, *args, **kwargs):
        user = User.objects.get(id='the_user_id')
        user.favorites.values('training')


class FavoriteTrainingListAPIView(ListAPIView):
    queryset = FavoriteTraining.objects.all()
    serializer_class = FavoriteTrainingSerializer
    lookup_field = 'id'

