from django import forms
from django.contrib.auth.forms import UserCreationForm

from new_app.models import Login, StudentRegister, Complaint, Notification


class Login_Form(UserCreationForm):
    class Meta:
        model = Login
        fields = ("username","password1","password2")


class StudentRegisterForm(forms.ModelForm):

    class Meta:
        model = StudentRegister
        fields =('__all__')
        exclude = ('user',)


class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ('__all__')
        exclude = ('status','reply',)

class NotificationForm(forms.ModelForm):
    class Meta:
        model = Notification
        fields = ('__all__')
        exclude = ('reply',)

