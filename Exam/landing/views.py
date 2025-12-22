from django.views.generic.edit import FormView
from django.http import JsonResponse
from .forms import ContactForm


class LandingFormView(FormView):
    template_name = 'landing/index.html'
    form_class = ContactForm

    def form_valid(self, form):
        """
        Обработка валидной формы.
        Возвращает JSON с данными формы,
        IP-адресом клиента и User-Agent.
        """
        request = self.request

        # Получение IP-адреса клиента
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')

        # Получение информации о браузере и системе
        user_agent = request.META.get('HTTP_USER_AGENT', 'Unknown')

        return JsonResponse({
            'status': 'success',
            'data': form.cleaned_data,
            'ip': ip,
            'user_agent': user_agent,
        })

    def form_invalid(self, form):
        """
        Обработка невалидной формы.
        Возвращает JSON с ошибками валидации.
        """
        return JsonResponse({
            'status': 'error',
            'errors': form.errors,
        }, status=400)