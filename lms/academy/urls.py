from django.urls import path, include, path
from rest_framework.routers import DefaultRouter
from django.contrib.auth import views as auth_views
from . import views

router = DefaultRouter()
router.register(r'products', views.ProductViewSet)
router.register(r'lessons', views.LessonViewSet)
router.register(r'user-lessons', views.UserLessonViewSet)

urlpatterns = [
    path('api/user-lessons/', views.UserLessonListView.as_view(), name='user-lesson-list'),
    path('api/products/<int:product_id>/lessons/', views.ProductLessonListView.as_view(), name='product-lesson-list'),
    path('api/product-stats/', views.ProductStatsView.as_view(), name='product-stats'),
    path('', views.index, name='index'),
    path('', include(router.urls)),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/profile/', views.profile, name='profile'),
    path('create/', views.create_product, name='create_product'),
    path('edit/<int:pk>/', views.edit_product, name='edit_product'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
]
