from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'products', views.ProductViewSet)
router.register(r'lessons', views.LessonViewSet)
router.register(r'user-lessons', views.UserLessonViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
