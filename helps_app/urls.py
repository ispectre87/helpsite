from . import views
from django.urls import path

app_name = 'helps_app'

urlpatterns = [
    path('', views.HelpHomepage.as_view(), name='index'),
    path('registration/', views.Registration.as_view(), name='registration'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('<int:region_id>/', views.CitiesList.as_view(), name='cities'),
    path('<int:region_id>/<int:city_id>/', views.HelpRequests.as_view(), name='help_requests'),
    path('help_request_detail/<int:help_id>/', views.HelpRequestDetail.as_view(), name='help_request_detail'),
    path('need_help/<int:city_id>/', views.need_help, name='need_help'),
    path('request_added/', views.request_added, name='request_added'),


]