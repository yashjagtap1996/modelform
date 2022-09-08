from django import forms

from Studentapp.models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields="__all__"
        labels={'email':'Enter Email','password':'Enter Password',
               'address':'Enter Address','state':'Enter State','zip':
               'Zip-Code','mark':'Check-In'}
