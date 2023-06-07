from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'cart'

urlpatterns = [
    path('', views.cart_detail, name='cart_details'),
    path('add/<int:issue_id>/',
         views.cart_add,
         name='cart_add'),
    path('remove/<int:issue_id>/',
         views.cart_remove,
         name='cart_remove')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)