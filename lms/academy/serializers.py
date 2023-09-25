from rest_framework import serializers
from .models import Product, Lesson, UserLesson


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class UserLessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLesson
        fields = '__all__'


# new
class ProductStatsSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    product_name = serializers.CharField()
    lesson_count = serializers.IntegerField()
    total_watch_time = serializers.IntegerField()
    total_users = serializers.IntegerField()
    purchase_percentage = serializers.FloatField()
