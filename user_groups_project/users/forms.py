from django import forms
from .models import User
from groups.models import Group
class UserForm(forms.ModelForm):
    group = forms.ModelChoiceField(queryset=Group.objects.all(), empty_label=None)

    class Meta:
        model = User
        fields = ['name', 'group']

    widgets = {
        'username': forms.TextInput(attrs={'class': 'custom-input'}),
        'group': forms.Select(attrs={'class': 'custom-select'}),
    }