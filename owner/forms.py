from django import forms
from django.contrib.auth.models import User
from .models import user
from .models import Menu



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
        



class menuform(forms.ModelForm):
  
    # create meta class
    class Meta():
        # specify model to be used
        model = Menu
  
        # specify fields to be used
        fields = ('Menu_id','Name','category','Price')
        labels = {'Name':'Enter Name' , 'category':'Enter category','Price':'Enter Price'}
    