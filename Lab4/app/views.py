from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
import random

from .forms import TemplateForm, CustomUserCreationForm


def template_view(request):
    if request.method == "POST":
        form = TemplateForm(request.POST)
        if form.is_valid():
            return JsonResponse(form.cleaned_data)

        return render(request, "app/template_form.html", {"form": form})

    return render(request, "app/template_form.html", {"form": TemplateForm()})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("app:user_profile")

        return render(request, "app/login.html", {"form": form})

    return render(request, "app/login.html", {"form": AuthenticationForm()})


def logout_view(request):
    logout(request)
    return redirect("app:login")


def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend="django.contrib.auth.backends.ModelBackend")
            return redirect("app:user_profile")

        return render(request, "app/register.html", {"form": form})

    return render(request, "app/register.html", {"form": CustomUserCreationForm()})


def user_profile(request):
    return render(request, "app/user_details.html")


def get_text(request):
    wishes = [
        "🎄 Тебя ждёт момент, когда всё заработает… и ты не поймёшь почему.",
        "😂 Тебя ждёт успешная сдача лабы без слов «а вот тут давай переделаем».",
        "☕ Тебя ждёт ночь, когда ты закроешь ноутбук раньше 3 утра.",
        "🐍 Тебя ждёт Python, который внезапно станет понятным.",
        "💥 Тебя ждёт осознание, что ошибка была в одном символе.",
        "🎁 Тебя ждёт «зачтено» быстрее, чем pip install django.",
        "😎 Тебя ждёт код, который запускается с первого раза (да, это возможно).",
        "📉 Тебя ждёт резкое падение стресса после сдачи лабы.",
        "🧠 Тебя ждёт фраза: «А, так вот как это работает».",
        "🎉 Тебя ждёт чувство, будто ты хакнул систему обучения."
    ]

    return JsonResponse({
        "text": random.choice(wishes)
    })