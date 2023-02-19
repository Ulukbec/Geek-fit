from django.urls import path
from . import views

urlpatterns = [
    path('personal_inform_view/', views.PersonalInformAPIView.as_view()),
    path('personal_inform_detail/<int:id>/', views.PersonalInformRUDAPIView.as_view()),
    path('my_card/', views.MyCardAPIView.as_view()),
    path('my_card/<int:id>/', views.MyCardRUDAPIView.as_view()),
]
