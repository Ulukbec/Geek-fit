from django.urls import path
from . import views


urlpatterns = [
    path('personal_inform_view/', views.PersonalInformAPIView.as_view()),
    path('personal_inform_edit/<int:id>/', views.PersonalInformRUAPIView.as_view()),
    path('my_card/', views.MyCardAPIView.as_view()),
    path('profile_email/', views.EmailProfileView.as_view()),
    path('my_card/<int:id>/', views.MyCardRUAPIView.as_view()),
]
