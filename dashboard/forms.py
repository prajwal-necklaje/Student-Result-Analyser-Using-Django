from django import forms
from dashboard.models import Ra

class OrderForm(forms.ModelForm):
    class Meta:
        model = Ra
        fields = ['student', 'classes', 'subject', 'marks']
