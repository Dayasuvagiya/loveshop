from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="home.html"), name='home'),  # Home page
    path('accounts/', include('accounts.urls')),  # Include the accounts app URLs
    path('products/', include('products.urls', namespace='products')),  # Products app
    path('contact/', include('contact.urls', namespace='contact')),  # Contact app
    path('checkout/', include('checkout.urls', namespace='checkout')),  # Checkout app
]