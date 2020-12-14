from django import forms
from django.core import validators


class FormArticle(forms.Form):
    title = forms.CharField(
        label = "Titulo",
        max_length=20,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder':'Ingresa un Titulo',
                'class':'titulo_form_article',
                'autocomplete':'off'
            }
        ),
        validators=[
            validators.MinLengthValidator(4,'El Titulo es demasiado Corto'),
            validators.RegexValidator('^[A-Za-z0-9 ]*$','El titulo esta mal formado','invalid_title')
        ]
    )

    content = forms.CharField(
        label = "Contenido",
        required=True,
        widget=forms.Textarea(
            attrs={
                'placeholder':'Ingresa un Contenido',
                'class':'contenido_form_article',
                'autocomplete':'off',
                'id':'contenido_form'
            }
        ),
        validators=[
            validators.MaxLengthValidator(80,'Has ingresado demasiados caracteres')
        ]
    )
  
    public_options = [
        (1,'Si'),
        (0,'No')
    ]

    public = forms.TypedChoiceField(
        label = "¿Publicado?",
        choices =  public_options
    )