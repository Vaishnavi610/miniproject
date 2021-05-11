from .models import user, Payment ,Menu,Transaction

from django.contrib import admin
# Register your models here.

class MenuAdmin(admin.ModelAdmin):
   
    list_display=("Menu_id","Name","Price", "category")

class userAdmin(admin.ModelAdmin):
               
    list_display=("id","first_name",'last_name','Mobile','department','Pay_mode','Time_mode')

class TransactionAdmin(admin.ModelAdmin):
    list_display=("Member_id","Menu_id","Quantity")



admin.site.register(user,  userAdmin)
admin.site.register(Payment)
admin.site.register(Menu, MenuAdmin)
admin.site.register(Transaction,TransactionAdmin)

