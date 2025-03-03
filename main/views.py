from django.shortcuts import render

def index(request):

    context = {
        'title': 'ДПО - Главная',
        'content': "",
        'is_superuser': request.user.is_superuser,
    }

    return render(request, 'main/index.html', context)


def curse_cart(request):

    context = {
        'title': 'ДПО - Главная',
        'content': "",
    }

    return render(request, 'main/curse_cart.html', context)

def students(request):

    context = {
        'title': 'ДПО - Главная',
        'content': "",
    }

    return render(request, 'main/students_curses_list.html', context)


