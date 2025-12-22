"""
WSGI config for project project.

Этот файл используется для запуска Django-приложения
на production-серверах (gunicorn, uWSGI и т.д.).

Для учебной лабораторной работы изменений не требует.
"""

import os
from django.core.wsgi import get_wsgi_application

# Указываем Django, где находятся настройки проекта
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

# WSGI-приложение
application = get_wsgi_application()