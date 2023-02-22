from django.contrib import admin
from django.urls import path
from geeksfit import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('trainings/', views.TrainingModelViewSet.as_view()),
    path('trainings/<int:id>/', views.TrainingDetailView.as_view()),
    path('favotiet/', views.FavoriteView.as_view())
]
