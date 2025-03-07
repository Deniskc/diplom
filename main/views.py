from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from main.forms import RequestEducationForm
from main.models import Curses, Documents, Students


def index(request):

    curses = Curses.objects.all()
    
    if request.method == 'POST':
        form = RequestEducationForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('main:index'))      
    else:
        form = RequestEducationForm()

    context = {
        'title': 'ДПО - Главная',
        'content': "",
        'is_superuser': request.user.is_superuser,
        'curses': curses,
        'form': form,

    }


    return render(request, 'main/index.html', context)

def curse_cart(request, curse_slug):

    curse = Curses.objects.get(slug=curse_slug)
    documents = Documents.objects.all()

    context = {
        'title': 'ДПО - Главная',
        'content': "",
        'curse': curse,
        'documents': documents,
    }

    return render(request, 'main/curse_cart.html', context)

def students(request):

    students = Students.objects.all()
    
    context = {
        'title': 'ДПО - Главная',
        'content': "",
        'students': students,
    }

    return render(request, 'main/students_curses_list.html', context)

