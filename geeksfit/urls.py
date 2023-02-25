from django.contrib import admin
from django.urls import path
from geeksfit import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('trainings/', views.TrainingModelViewSet.as_view()),
    path('trainings/<int:id>/', views.TrainingDetailView.as_view()),
    path('favoritetrainings/', views.FavoriteTrainingListAPIView.as_view()),
    path('favoritetrainings/<int:id>/', views.FavoriteTrainingRetrieveAPIView.as_view()),
]
