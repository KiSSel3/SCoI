from django.urls import path
from .import views

app_name = 'services'

urlpatterns = [
    path('', views.all_devices_view.as_view(), name='home'),
    path('services', views.services, name="services"),
    path('create', views.create, name='create'),
    path('createIssue',views.create_issue,name='createIssue'),
    path('edit/<int:id>/',views.issue_edit,name='editIssue'),
    path('details/<int:id>/',views.detail,name='detail')
]

