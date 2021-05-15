from .models import user, Payment, Menu, Transaction, Absent

from django.contrib import admin
# Register your models here.

class MenuAdmin(admin.ModelAdmin):
   
    list_display=("Menu_id","Name","Price", "Category")

class userAdmin(admin.ModelAdmin):
               
    list_display = ("user_id", 
                    'Mobile', 'Department', 'Pay_mode', 'Time_mode')

class TransactionAdmin(admin.ModelAdmin):
    list_display=("Member_id","Menu1_id","Quantity","Amount","Paid","Date_added")


class AbsentAdmin(admin.ModelAdmin):

    list_display = ("id",
                    "Time", "Day", "From_date", "To_date")

class PaymentAdmin(admin.ModelAdmin):
    list_display=("Member_id","Amount_paid","Date_added")


admin.site.register(user,  userAdmin)
admin.site.register(Payment,PaymentAdmin)
admin.site.register(Menu, MenuAdmin)
admin.site.register(Transaction,TransactionAdmin)
admin.site.register(Absent, AbsentAdmin)
