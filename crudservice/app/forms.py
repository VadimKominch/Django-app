from django import forms
from django.forms import fields
from .models import Employee

class EmployeeForm(forms.ModelForm):
    name = forms.CharField(max_length=30,label="Имя:")
    surname = forms.CharField(max_length=30,label="Фамилия:")

    class Meta:
        model = Employee
        fields = ['name','surname']