from . import views
from django.urls import path

app_name = 'helps_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('help_requests/', views.help_requests, name='help_requests'),
    path('help_requests/<int:title_id>/', views.help_request_detail, name='help_request_detail'),
    path('need_help/', views.need_help, name='need_help'),
    path('request_added/', views.request_added, name='request_added')

]