from .models import user, Payment, Menu, Transaction, Absent

from django.contrib import admin
# Register your models here.

class MenuAdmin(admin.ModelAdmin):
   
    list_display=("Menu_id","Name","Price", "category")

class userAdmin(admin.ModelAdmin):
               
    list_display = ("user_id", 
                    'Mobile', 'department', 'Pay_mode', 'Time_mode')

class TransactionAdmin(admin.ModelAdmin):
    list_display=("Member_id","Menu1_id","Quantity","Paid")


class AbsentAdmin(admin.ModelAdmin):

    list_display = ("id",
                    "Time", "Day", "From_date", "To_date")


admin.site.register(user,  userAdmin)
admin.site.register(Payment)
admin.site.register(Menu, MenuAdmin)
admin.site.register(Transaction,TransactionAdmin)
admin.site.register(Absent, AbsentAdmin)
