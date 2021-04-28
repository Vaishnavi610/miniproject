from django.urls import path
from . import views as views


urlpatterns = [
    path("", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("main/", views.main, name="main"),
    path("add_member/", views.add_member, name="add_member"),
    path("pay_history/", views.pay_history, name="pay_history"),
    path("menu/", views.menu, name="menu"),
    path("search/", views.search, name="search"),
    path("menu2/", views.menu2, name="menu2"),
    path("home/", views.home, name="home"),
    path("index/", views.index, name="index"),
    path("about_us/", views.about_us, name="about_us"),
    path("feedback/", views.feedback, name="feedback"),
    path("about_us2/", views.about_us2, name="about_us2"),
    path("feedback2/", views.feedback2, name="feedback2"),
    path("pay_history2/", views.pay_history2, name="pay_history2"),
    path("home2/", views.home2, name="home2"),
    path("members_data/", views.member, name="members_data"),
    path("add_menu/", views.add_menu, name="add_menu"),
    path("delete/<int:id>", views.delete_menu, name="deletemenu"),
    path("<int:id>/", views.update_menu, name="updatemenu"),
    path("notcome/", views.notcome, name="notcome"),
    path("absent/", views.absent, name="absent"),
  
]
