from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

# Wire up the API using automatic URL routing.
router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')

urlpatterns = [
    path('', include(router.urls)),
]
