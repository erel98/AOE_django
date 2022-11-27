from django.forms import ModelForm, widgets
from .models import User


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        widgets = {
            'first_name': widgets.TextInput(attrs={'class':'form-control'}),
            'last_name': widgets.TextInput(attrs={'class':'form-control'}),
            'email': widgets.TextInput(attrs={'class':'form-control'}),
            'phone': widgets.TextInput(attrs={'class':'form-control'}),
            'date': widgets.DateInput(attrs={'class':'form-control'}),
        }



