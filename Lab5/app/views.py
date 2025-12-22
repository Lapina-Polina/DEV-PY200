from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.views import View
from django.views.generic import TemplateView, FormView
from django.contrib.auth.views import LoginView
import random

from .forms import TemplateForm, CustomUserCreationForm


# =====================
# INDEX
# =====================
def index_view(request):
    return render(request, "app/index.html")


# =====================
# FUNCTION VIEW (1.0)
# =====================
def template_view(request):
    if request.method == "POST":
        form = TemplateForm(request.POST)
        if form.is_valid():
            return JsonResponse(form.cleaned_data)
        return render(request, "app/template_form.html", {"form": form})

    return render(request, "app/template_form.html", {"form": TemplateForm()})


# =====================
# CBV View (1.1)
# =====================
class TemplView(View):
    def get(self, request):
        form = TemplateForm()
        return render(request, "app/template_form.html", {"form": form})

    def post(self, request):
        form = TemplateForm(request.POST)
        if form.is_valid():
            return JsonResponse(form.cleaned_data)
        return render(request, "app/template_form.html", {"form": form})


# =====================
# TemplateView (1.2) — GET + POST
# =====================
class MyTemplView(TemplateView):
    template_name = "app/template_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = TemplateForm()
        return context

    def post(self, request, *args, **kwargs):
        form = TemplateForm(request.POST)

        if form.is_valid():
            return JsonResponse(form.cleaned_data)

        context = self.get_context_data(**kwargs)
        context["form"] = form
        return self.render_to_response(context)


# =====================
# FormView (1.3) — ОСНОВНОЕ
# =====================
class MyFormView(FormView):
    template_name = "app/template_form.html"
    form_class = TemplateForm
    success_url = "/"

    def form_valid(self, form):
        return JsonResponse(form.cleaned_data)


class MyLoginView(LoginView):
    template_name = "app/login.html"
    redirect_authenticated_user = True

# =====================
# LOGIN
# =====================
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("app:user_profile")
        return render(request, "app/login.html", {"form": form})

    return render(request, "app/login.html", {"form": AuthenticationForm()})


# =====================
# REGISTER
# =====================
def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(
                request,
                user,
                backend="django.contrib.auth.backends.ModelBackend",
            )
            return redirect("app:user_profile")

        return render(request, "app/register.html", {"form": form})

    return render(request, "app/register.html", {"form": CustomUserCreationForm()})


# =====================
# LOGOUT
# =====================
def logout_view(request):
    logout(request)
    return redirect("app:login")


# =====================
# PROFILE
# =====================
def user_detail_view(request):
    return render(request, "app/user_details.html")


# =====================
# PASSWORD RESET (ЗАГЛУШКА)
# =====================
def reset_view(request):
    return render(request, "app/password_reset_form.html")


# =====================
# AJAX JSON
# =====================
def get_text_json(request):
    wishes = [
        "🎄 Тебя ждёт момент, когда всё заработает… и ты не поймёшь почему.",
        "😂 Тебя ждёт успешная сдача лабы без слов «а вот тут давай переделаем».",
        "☕ Тебя ждёт ночь, когда ты закроешь ноутбук раньше 3 утра.",
        "🐍 Тебя ждёт Python, который внезапно станет понятным.",
        "💥 Тебя ждёт осознание, что ошибка была в одном символе.",
        "🎁 Тебя ждёт «зачтено» быстрее, чем pip install django.",
        "😎 Тебя ждёт код, который запускается с первого раза.",
        "📉 Тебя ждёт резкое падение стресса после сдачи лабы.",
        "🧠 Тебя ждёт фраза: «А, так вот как это работает».",
        "🎉 Тебя ждёт чувство, будто ты хакнул систему обучения.",
    ]

    return JsonResponse({
        "text": random.choice(wishes)
    })
