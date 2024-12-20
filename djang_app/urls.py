from django.urls import path
from . import views,views_login
urlpatterns = [
    # home
    path('',views_login.log_in,name="home"),
    # create
    path('form',views.addStudy,name="form"),
    # list
    path('list',views.view,name="list"),
    # edit
    path('edited/<pk>',views.edit,name="re_create"),
    # delete
    path('delete/<pk>',views.delete,name="delete")

]
