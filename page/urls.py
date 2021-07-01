
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='login'),
    path('signup/',views.signup,name='signup'),
   
    path('logout',views.logout,name='logout'),
    path('modify',views.modify,name='modify'),
]