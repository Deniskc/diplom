from django.urls import path

from main import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('toggle_theme/', views.toggle_theme, name='toggle_theme'),
    path('curse/<slug:curse_slug>/', views.curse_cart, name='curse_cart'),
    path('students/', views.students, name='students'),
    path('get_file/', views.export_to_csv, name='get_file'),
    path('news/<slug:news_slug>', views.news, name='news'),
]
