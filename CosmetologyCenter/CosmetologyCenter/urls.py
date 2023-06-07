from django.contrib import admin
from django.urls import path, include

urlpatterns = [
     path('admin/', admin.site.urls),
     path('', include('services.urls', namespace='services')),
     path('auth/', include('login.urls', namespace='login')),
     path('cart/', include('cart.urls', namespace='cart')),
     path('order/', include('order.urls', namespace='order')),
]
