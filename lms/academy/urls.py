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
    path('api/user-lessons/', views.UserLessonListView.as_view(), name='user-lesson-list'),
    path('api/products/<int:product_id>/lessons/', views.ProductLessonListView.as_view(), name='product-lesson-list'),
    path('api/product-stats/', views.ProductStatsView.as_view(), name='product-stats'),
]
