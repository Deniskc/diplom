from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from main.forms import RequestEducationForm
from main.models import Curses, Documents, News, NewsTag, Students
import csv
import random as r

def index(request):

    # selected_curse = request.POST.get('id_curse')

    news = News.objects.all().order_by('-date')

    if len(News.objects.all()) > 3:
        news = News.objects.all().order_by('-date')[:3]


    curses = Curses.objects.all()
    len_curses_is_even = False
    if len(Curses.objects.all())%2 == 0:
        len_curses_is_even = True

    last_index = len(Curses.objects.all())-1
    last_curse = Curses.objects.all()[last_index]
    
    if request.method == 'POST':
        form = RequestEducationForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('main:students'))      
    else:
        form = RequestEducationForm()

    context = {
        'title': 'ДПО - Главная',
        'content': "",
        'is_superuser': request.user.is_superuser,
        'curses': curses,
        'form': form,
        'last_curse': last_curse,
        'len_curses_is_even': len_curses_is_even,
        'news':news,
    }

    return render(request, 'main/index.html', context)

def curse_cart(request, curse_slug):

    curse = Curses.objects.get(slug=curse_slug)
    documents = Documents.objects.all()

    context = {
        'title': 'ДПО - Курсы',
        'content': "",
        'curse': curse,
        'documents': documents,
    }

    return render(request, 'main/curse_cart.html', context)

def students(request):

    students = Students.objects.all()
    rand_list = [r.randint(1111,9999) for i in range(0,len(Students.objects.all()))]
    
    context = {
        'title': 'ДПО - Поступающим',
        'content': "",
        'students': students,
    }

    return render(request, 'main/students_curses_list.html', context)

def news(request, news_slug):

    news = News.objects.get(slug=news_slug)
    recent_news = News.objects.exclude(slug=news_slug)
    if len(recent_news) > 3:
        recent_news = News.objects.exclude(slug=news_slug)[:3]

    all_news_tags = NewsTag.objects.all()
    news_tags = NewsTag.objects.filter(new_id=news.id)
    
    
    context = {
        'title': 'ДПО - Новости',
        'content': "",
        'news': news,
        'recent_news': recent_news,
        'news_tags': news_tags,
        'all_news_tags': all_news_tags,
    }

    return render(request, 'main/single.html', context)

def export_to_csv(request):
    # Создаем HTTP-ответ с типом содержимого 'text/csv'
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="students.csv"'

    # Создаем объект writer для записи в CSV
    writer = csv.writer(response)

    # Записываем заголовки столбцов
    writer.writerow([
        'Фамилия',
        'Имя',
        'Отчество',
        'Дата рождения',
        'Программа обучения',
        '№ заявления',
        'Бюджет/Внебюджет',
        'Форма обучения',
        'Эл. почта',
        'Телефон',
        'Примечания',
        'Оплачен курс?'
    ]) 

    # Получаем данные из модели
    queryset = Students.objects.all()

    # Записываем данные в CSV
    for obj in queryset:
        numb_statement = 'К-0000' + str(obj.id) 
        writer.writerow([
            obj.last_name,
            obj.first_name,
            obj.surname,
            obj.birth_date,
            obj.curse,
            numb_statement,
            obj.curse.paid_or_free,
            obj.curse.edu_form,
            obj.email,
            obj.phone,
            obj.description,
            obj.curse_is_paid,
        ]) 

    return response

