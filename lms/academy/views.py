from rest_framework import viewsets, generics
from .models import Product, Lesson, UserLesson
from .serializers import ProductSerializer, LessonSerializer, UserLessonSerializer

from .serializers import ProductStatisticsSerializer
from django.db.models import Sum, Count, F


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
class UserLessonsList(generics.ListAPIView):
    serializer_class = LessonSerializer

    def get_queryset(self):
        user = self.request.user
        return Lesson.objects.filter(products__owner=user, userlesson__user=user)


class UserProductLessonsList(generics.ListAPIView):
    serializer_class = UserLessonSerializer

    def get_queryset(self):
        user = self.request.user
        product_id = self.kwargs['product_id']
        return UserLesson.objects.filter(user=user, lesson__products=product_id)


class ProductStatisticsList(generics.ListAPIView):
    serializer_class = ProductStatisticsSerializer

    def get_queryset(self):
        return Product.objects.annotate(
            total_viewed_lessons=Count('lessons__userlesson', filter=F('lessons__userlesson__viewed')),
            total_view_time=Sum('lessons__userlesson__view_time_seconds'),
            total_students=Count('lessons__userlesson__user', distinct=True),
            purchase_percentage=(Count('accesses') / Count('lessons__userlesson__user', distinct=True)) * 100
        )