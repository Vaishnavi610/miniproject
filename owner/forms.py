from django import forms
from django.contrib.auth.models import User
from .models import user



class userform(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('id','username','password','email')

##class for extra field
class info(forms.ModelForm):
    class Meta():
        model = user
        fields = ('first_name','last_name','Mobile','department','Pay_mode','Time_mode')
        




    