from django.urls import path
from . import views


urlpatterns = [
    path('trainings/', views.TrainingModelViewSet.as_view()),
    path('trainings/<int:id>/', views.TrainingDetailView.as_view()),
    path('favoritetrainings/', views.FavoriteTrainingListAPIView.as_view()),
    path('favoritetrainings/<int:id>/', views.FavoriteTrainingListAPIView.as_view()),
]
