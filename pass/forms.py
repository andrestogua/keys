from django import forms

from .models import PassModel

class PassForm(forms.ModelForm):
    
    class Meta:
        model = PassModel
        fields = ("account","password")
        labels = {
            'account':'Cuenta',
            'password':'Contraseña'
        }
        widget = {
            'descripcion': forms.TextInput,
            'password': forms.TextInput,
            }
    
        def __init__(self,*args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update({
                    'class':'form-coontrol'
                })
