from django import forms
from .models import User
from groups.models import Group


class UserForm(forms.ModelForm):
    group = forms.ModelChoiceField(queryset=Group.objects.all(), empty_label=None)

    class Meta:
        model = User
        fields = ['name', 'group']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'group': forms.Select(attrs={'class': 'form-select'})
        }
