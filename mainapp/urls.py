from django.contrib import admin
from django.urls import path
from django.urls import include
import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.accommodations, name='index'),
    #path('accommodations/<int:pk>/', mainapp.accommodations,
         #name='accommodations'),
    #path('accommodations/<int:pk>/page/<int:page>/', mainapp.accommodations,
         #name='page'),
    path('auth/', include('authapp.urls', namespace='auth')),
    path('accommodation_details/<int:pk>/', mainapp.accommodation,
         name='accommodation'),

]
