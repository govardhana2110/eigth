from django.urls import path
from dbapp import views
app_name='dbapp'
urlpatterns=[
    path('',views.input,name='input'),
    path('insert',views.insert,name='insert'),
    path('display',views.display,name='display'),

]