from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'products', views.ProductViewSet)
router.register(r'lessons', views.LessonViewSet)
router.register(r'user-lessons', views.UserLessonViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # new
    path('api/user-lessons/', views.UserLessonsList.as_view(), name='user-lessons-list'),
    path('api/user-product-lessons/<int:product_id>/', views.UserProductLessonsList.as_view(),
         name='user-product-lessons-list'),
    path('api/product-statistics/', views.ProductStatisticsList.as_view(), name='product-statistics-list'),
]
