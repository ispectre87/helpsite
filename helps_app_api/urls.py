from . import views
from django.urls import path

app_name = 'helps_app_api'

urlpatterns = [
    path('helps/', views.HelpRequestsApiView.as_view()),
    path('helps/<int:pk>', views.HelpRequestsApiUpdate.as_view()),
    path('city/', views.CityApiView.as_view()),
    path('city/<int:pk>', views.CityApiUpdate.as_view()),
    path('region/', views.RegionApiView.as_view()),
    path('region/<int:pk>', views.RegionApiUpdate.as_view()),

    # path('tws/', views.HelpRequestsApiViewNoSerializer.as_view()),
    # path('wsr/', views.HelpRequestApiWithSerializer.as_view()),
    # path('region/', views.RegionApiView.as_view()),
    # path('region/<int:pk>', views.RegionApiView.as_view()),
]