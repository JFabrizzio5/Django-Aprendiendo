from django import forms

class MensajeForm(forms.Form):
    mensaje = forms.CharField(label='Mensaje', max_length=100)
