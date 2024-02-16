from django.urls import path
from . import views

app_name = 'contact'

urlpatterns = [
    path('', views.contact_page, name='index'),  # Assuming a view named contact_page
    path('contact_success/', views.contact_success, name='contact_success'),
    
]