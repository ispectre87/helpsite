from . import views
from django.urls import path

app_name = 'helps_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:region_id>/', views.cities, name='cities'),
    path('<int:region_id>/<int:city_id>/', views.help_requests, name='help_requests'),
    path('help_request_detail/<int:help_id>/', views.help_request_detail, name='help_request_detail'),
    path('need_help/<int:city_id>/', views.need_help, name='need_help'),
    path('request_added/', views.request_added, name='request_added'),

]