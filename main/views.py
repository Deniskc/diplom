from django.shortcuts import render

def index(request):

    context = {
        'title': 'DMShop - Главная',
        'content': "",
    }

    return render(request, 'main/index.html', context)


def curse_cart(request):

    context = {
        'title': 'DMShop - Главная',
        'content': "",
    }

    return render(request, 'main/curse_cart.html', context)


