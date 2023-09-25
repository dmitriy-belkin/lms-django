from rest_framework import generics
from rest_framework import viewsets
from .models import Lesson, UserLesson, Product, UserAccess
from .serializers import ProductSerializer, LessonSerializer, UserLessonSerializer, ProductStatsSerializer

from django.db.models import Sum


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class UserLessonViewSet(viewsets.ModelViewSet):
    queryset = UserLesson.objects.all()
    serializer_class = UserLessonSerializer


# new
class UserLessonListView(generics.ListAPIView):
    serializer_class = UserLessonSerializer

    def get_queryset(self):
        user = self.request.user
        return UserLesson.objects.filter(user=user)


class ProductLessonListView(generics.ListAPIView):
    serializer_class = UserLessonSerializer

    def get_queryset(self):
        user = self.request.user
        product_id = self.kwargs['product_id']
        return UserLesson.objects.filter(user=user, lesson__product_id=product_id)


class ProductStatsView(generics.ListAPIView):
    serializer_class = ProductStatsSerializer

    def get_queryset(self):
        user = self.request.user
        products = Product.objects.all()
        queryset = []
        for product in products:
            access_count = UserAccess.objects.filter(product=product).count()
            lesson_count = UserLesson.objects.filter(lesson__product=product, user=user).count()
            total_watch_time = UserLesson.objects.filter(lesson__product=product, user=user).aggregate(Sum('watch_time'))['watch_time__sum']
            total_users = UserAccess.objects.filter(product=product).count()
            purchase_percentage = (access_count / total_users) * 100 if total_users > 0 else 0

            queryset.append({
                'product_id': product.id,
                'product_name': product.name,
                'lesson_count': lesson_count,
                'total_watch_time': total_watch_time,
                'total_users': total_users,
                'purchase_percentage': purchase_percentage,
            })
        return queryset
