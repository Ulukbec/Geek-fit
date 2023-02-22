from django.contrib import admin
from django.urls import path, include
from . import yasg
from apps.geeksfit.api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('trainings', views.TrainingModelViewSet)
router.register('categories', views.CategoryModelViewSet)
router.register('reviews', views.ReviewModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    # path('api/v1/users/', include('apps.users.api.urls'))
]

urlpatterns += yasg.urlpatterns
