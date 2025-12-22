from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        required=True,
        label='Имя',
    )
    email = forms.EmailField(
        required=True,
        label='Email',
    )
    message = forms.CharField(
        required=True,
        max_length=1000,
        widget=forms.Textarea,
        label='Сообщение',
    )

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name.strip():
            raise forms.ValidationError('Имя не может быть пустым.')
        return name