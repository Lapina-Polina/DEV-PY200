from django import forms
from django.contrib.auth.forms import UserCreationForm


class TemplateForm(forms.Form):
    email = forms.EmailField(label="Email")
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput
    )
    birth_date = forms.DateField(
        label="Дата рождения",
        required=False,
        widget=forms.DateInput(attrs={"type": "date"})
    )
    count = forms.IntegerField(
        label="Количество",
        min_value=1
    )
    agree = forms.BooleanField(
        label="Согласен с условиями",
        required=False
    )


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(label="Email")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]

        if commit:
            user.save()
            if hasattr(self, "save_m2m"):
                self.save_m2m()

        return user