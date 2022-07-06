from . import views
from django.urls import path

app_name = 'helps_app_api'

urlpatterns = [
    path('test/', views.HelpRequestsApiView.as_view()),
    path('tws/', views.HelpRequestsApiViewNoSerializer.as_view()),
    path('wsr/', views.HelpRequestApiWithSerializer.as_view()),
    path('region/', views.RegionApiView.as_view()),
    path('region/<int:pk>', views.RegionApiView.as_view()),
]