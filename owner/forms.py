from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import user
from .models import Menu,Transaction
from .models import *

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['id','username','first_name','last_name','email', 'password1', 'password2']



##class for extra field
class info(forms.ModelForm):
    class Meta():
        model = user
        fields = ('Mobile','Department','Pay_mode','Time_mode')
        



class menuform(forms.ModelForm):
  
    # create meta class
    class Meta():
        # specify model to be used
        model = Menu
  
        # specify fields to be used
        fields = ('Menu_id','Name','Category','Price')
        labels = {'Name':'Enter Name' , 'Category':'Enter category','Price':'Enter Price'}
    

class transactionform(forms.ModelForm):
    class Meta():
        model = Transaction
        fields  = ('id','Menu1_id', 'Quantity', 'Paid')
        #labels = {'Paid': 'Paid', 'Menu_id': 'menu'}


class DateInput(forms.DateInput):
    input_type = 'date'


class absentform(forms.ModelForm):
    class Meta:
        model = Absent
        fields = ( 'id','Time','Day', 'From_date', 'To_date')
        widgets = {
            'From_date': DateInput(),
            'To_date' : DateInput()
        }


class EditUserProfileForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = {'username', 'first_name', 'last_name',
                  'email', 'date_joined', 'last_login'}
        labels = {'email': 'Email'}


class paymentform(forms.ModelForm):
    class Meta():
        model = Payment
        fields  = ('Amount_paid',)
        
