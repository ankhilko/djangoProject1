from django.forms import Form, EmailField, CharField, Textarea, TextInput, EmailInput, ModelForm

from blog.models import Contact


class ContactForm(ModelForm):
    name = CharField(
        widget=TextInput(
            attrs={
                'class': 'form-control',
                'id': 'name',
                'placeholder': 'Enter your name',
            }
        ),
        max_length=64,
    )
    email = EmailField(
        widget=EmailInput(
            attrs={
                'class': 'form-control',
                'id': 'email',
                'placeholder': 'Enter your E-Mail',
            }
        ),
        max_length=254,
    )
    message = CharField(
        widget=Textarea(
            attrs={
                'class': 'form-control',
                'id': 'message',
                'style': 'height: 12rem',
                'placeholder': 'Enter your message',
            }

        ),
        max_length=1024,
    )

    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']


