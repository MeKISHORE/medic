from django.contrib import admin
from django.urls import path,include
from.import views
urlpatterns = [
    path('', views.index, name='index'),
    path('RegisterHospital/', views.RegisterHospital, name='RegisterHospital'),
    # path('Hospital/', views.RegisterHospital, name='RegisterHospital'),
    path('Hospital_page/', views.Hospital_page, name='Hospital_page'),
    path('Maps/users/Apply/', views.User_form,name='User_form'),
    path('Maps/', views.maps,name='maps'),
    path('Hospital_page/updatehospital/', views.updatehospital,name='updatehospital'),
    path('Maps/users/Apply/emergency',views.emergency,name='emergency'),
    path('Hospital_page/approve',views.approve,name='approve'),

]
