from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import generics, viewsets
from django.http import JsonResponse
from .models import Lesson, UserLesson, Product, UserAccess
from .forms import ProductForm
from django.contrib.auth import authenticate, login
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
            total_watch_time = UserLesson.objects.filter(lesson__product=product,
                                                         user=user).aggregate(Sum('watch_time'))['watch_time__sum']
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


def index(request):
    products = Product.objects.all()
    lessons = Lesson.objects.all()
    user_lessons = UserLesson.objects.all()
    user_access = UserAccess.objects.all()

    context = {
        'products': products,
        'lessons': lessons,
        'user_lessons': user_lessons,
        'user_access': user_access,
    }

    return render(request, 'index.html', context)


def profile(request):
    user = request.user

    context = {
        'user': user,
    }

    return render(request, 'profile.html', context)


def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'create_product.html', {'form': form})


def edit_product(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'edit_product.html', {'form': form})


def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    lessons = Lesson.objects.filter(product=product)
    return render(request, 'product_detail.html', {'product': product, 'lessons': lessons})


def login_view(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return JsonResponse({'success': False, 'error_message': 'Неверные учетные данные'})

    return render(request, 'login.html')
