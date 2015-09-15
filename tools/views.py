from django import forms
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login


def staff_check(user):
    """A decorator to check if the user is member of staff"""
    return user.is_staff


def tools_login(request):
    """The login/logout view"""
    context = dict()
    if request.method == 'POST':
        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            print('valid')
            print(type(login_form.get_user))
            login(request, login_form.get_user())
            context.update({'success_login': True})
            return render(request, 'home/tools_home.html', context)
        else:
            print('not valid')
    else:
        login_form = AuthenticationForm()
    context.update({'login_form': login_form})
    return render(request, 'login/tools_login.html', context)


@user_passes_test(staff_check, login_url='/tools/login')
def tools_home(request):
    """
    Tools home page
    Displays the login view if the user isn't authenticated,
    user account informations otherwise
    """
    return render(request, 'home/tools_home.html', context)


@user_passes_test(staff_check, login_url='/tools/login/')
def tools_news(request):
    """
    News editing page
    Provides news adding/editing/removing tools
    """
    return render(request, 'news/tools_news.html', locals())
