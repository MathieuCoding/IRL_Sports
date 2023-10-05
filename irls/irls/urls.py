from django.contrib import admin
from django.urls import path, include
from irls_api import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'events', views.EventViewSet)
router.register(r'structures', views.StructureViewSet)
router.register(r'sports', views.SportViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]