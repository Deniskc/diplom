from django.urls import path

from main import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('curse/<slug:curse_slug>/', views.curse_cart, name='curse_cart'),
    path('students/', views.students, name='students'),
    path('news/<slug:news_slug>', views.news, name='news'),
]
