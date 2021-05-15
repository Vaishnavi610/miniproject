from django.db import models
from django.contrib.auth.models import User


# Create your models here
class user(models.Model):
    user_id = models.ForeignKey(User,default=None, null=True, on_delete=models.CASCADE)
    ##add extra field
    
    Mobile = models.IntegerField()
    Department = models.CharField(max_length=50, null=True)
    Pay_mode = models.CharField(max_length=50, null=True)
    Time_mode = models.CharField(max_length=50, null=True)
    
    def __str__(self):
        return str(self.user_id)

    

class Menu(models.Model):
    CATEGORY=(
        ('Beverages','Beverages'),
        ('Thali','Thali'),
        ('snaks', 'snacks')
    )
    Menu_id = models.AutoField(primary_key=True)
    Name= models.CharField(max_length=50, null=True)
    Price= models.IntegerField(default=1, null=True)
    Category= models.CharField(max_length=50, null=True, choices=CATEGORY)

    def __str__(self):
        return self.Name

class Transaction(models.Model):
    Member_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    Menu1_id = models.ForeignKey(Menu, on_delete=models.CASCADE, null=True)
    Date_added=models.DateTimeField(auto_now_add=True,null=True)
    Amount= models.IntegerField(default=1, null=True)
    Quantity=models.IntegerField(default=1)
    Paid = models.BooleanField(default=False)
    
    class Meta:
        ordering=['-Date_added']
    def __str__(self):
        return self.Member_id.username

class Payment(models.Model):
    CATEGORY = (
        ('Advance', 'Advance'),
        ('Due', 'Due')
    )
    Member_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    Amount_paid = models.IntegerField(default=1, null=True)
    Date_added = models.DateTimeField(auto_now_add=True, null=True)
  

class Absent(models.Model):
    TIME = (
        ('Day', 'Day'),
        ('Night', 'Night'),
        ('Both', 'Both')
    )
    SELECT = (
        ('Today', 'Today'),
        ('More', 'More')
    )
    Member_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    Time = models.CharField(max_length=50, null=True, choices=TIME)
    Day = models.CharField(max_length=50, null=True, choices=SELECT)
    From_date = models.DateField(null=True)
    To_date = models.DateField(null=True)


