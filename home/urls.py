from django.contrib import admin
from django.urls import path
from home import views

admin.site.site_header = "Ami Ice Cream Admin"
admin.site.site_title = "Ami Ice Cream Admin Portal"
admin.site.index_title = "Welcome to Ami Ice Creams "

urlpatterns = [
    path("",views.index, name='home'),
    path("about",views.about, name='about'),
    path("contact",views.contact, name='contact'),
    path("services",views.services, name='services')
    
]
