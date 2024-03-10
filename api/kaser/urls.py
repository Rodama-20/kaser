from django.urls import path, include

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register("users", views.UserViewSet, basename="user")
router.register("photos", views.PhotoViewSet, basename="photo")
router.register("albums", views.AlbumViewSet, basename="album")

urlpatterns = [
    path("", include(router.urls)),
]
