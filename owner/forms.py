from django import forms
from django.contrib.auth.forms  import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import user
from .models import Menu,Absent



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



class absentform(forms.ModelForm):
    class Meta:
        model = Absent
        fields = ('first_name','last_name','Time','Day','From_date','To_date')
           
class EditUserProfileForm(UserChangeForm) :
    password = None 
    class Meta:
        model=User
        fields = {'username','first_name','last_name','email','date_joined','last_login'} 
        labels = {'email':'Email'} 
        
