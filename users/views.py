from django.contrib import messages, auth
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from users.forms import UserLoginForm, UserRegistrationForm

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)

            session_key = request.session.session_key

            if user:
                auth.login(request, user)
                # messages.success(request, f"{username}, Вы вошли в аккаунт!")

                if request.POST.get('next', None):
                    return HttpResponseRedirect(request.POST.get('next'))

                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()

    context = {
        'title': 'DMShop - Авторизация',
        'form': form,

    }
    return render(request, 'users/login.html', context)

def register(request):

    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()

            session_key = request.session.session_key

            user = form.instance
            auth.login(request, user)

            # messages.success(request, f"{user.username}, Вы успешно зарегистрированы!")
            return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserRegistrationForm()

    context = {
        'title': 'DMShop - Регистрация',
        'form': form,
    }
    return render(request, 'users/register.html', context)

@login_required
def logout(request):
    auth.logout(request)
    # messages.success(request, f"{request.user.username}, Вы вышли из аккаунта!")
    return redirect(reverse('main:index'))