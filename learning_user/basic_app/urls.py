from django.conf.urls import url
from django.urls import include,path
from basic_app import views

#TEMPLATE URLS

app_name = 'basic_app'

urlpatterns=[
    path('',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login'),
]