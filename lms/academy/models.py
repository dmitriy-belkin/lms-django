from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(default='Описание отсутствует')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    duration = models.IntegerField(default=0)
    students = models.ManyToManyField(User, related_name='enrolled_courses', blank=True)

    def __str__(self):
        return self.name

    objects = models.Manager()


class Enrollment(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student.username} - {self.product.name}"


class Lesson(models.Model):
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    video_url = models.URLField()
    duration_seconds = models.IntegerField()
    products = models.ManyToManyField(Product, related_name='lessons')

    objects = models.Manager()


class UserLesson(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    viewed = models.BooleanField(default=False)
    view_time_seconds = models.IntegerField(default=0)
    video_progress = models.FloatField(default=0.0)

    objects = models.Manager()

    def update_video_progress(self, new_progress):
        self.video_progress = new_progress
        self.save()
        self.mark_as_viewed()

    def mark_as_viewed(self):
        if self.video_progress >= 80:
            self.viewed = True
        else:
            self.viewed = False
        self.save()


class UserAccess(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    objects = models.Manager()

    def __str__(self):
        # noinspection PyUnresolvedReferences
        return f"{self.user.username} - {self.product.name}"
