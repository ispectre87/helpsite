from . import views
from django.urls import path, include, re_path
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'city', views.CityApi)

app_name = 'helps_app_api'

urlpatterns = [
    path('helps/', views.HelpRequestsApiView.as_view()),
    path('helps/<int:pk>', views.HelpRequestsApiUpdate.as_view()),
    path('', include(router.urls)),
    re_path(r'^djoserauth/', include('djoser.urls')),
    re_path(r'^djoserauth/', include('djoser.urls.authtoken')),
    # path('city/', views.CityApi.as_view({'get': 'list', 'post': 'create'})),
    # path('city/<int:pk>', views.CityApi.as_view({'put': 'update', 'delete': 'destroy'})),
    path('region/', views.RegionApiView.as_view()),
    path('region/<int:pk>', views.RegionApiUpdate.as_view()),

    # path('tws/', views.HelpRequestsApiViewNoSerializer.as_view()),
    # path('wsr/', views.HelpRequestApiWithSerializer.as_view()),
    # path('region/', views.RegionApiView.as_view()),
    # path('region/<int:pk>', views.RegionApiView.as_view()),
]