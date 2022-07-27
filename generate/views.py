from django.shortcuts import render
import random
# Create your views here.


def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def password(request):
    characters = list('qazwsxedcrfvtgbyhnujmikolp')

    if request.GET.get('uppercase'):
        characters.extend(list('QAZWSXEDCRFVTGBYHNUJMIKOLP'))

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*=+-/*`()'))

    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))

    length = int(request.GET.get('length', 10))

    the_password = ""
    for i in range(length):
        the_password += random.choice(characters)
    return render(request, "password.html", {'password': the_password})
