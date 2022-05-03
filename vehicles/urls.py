from django.urls import path
from .views import UserVehicleListView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('vehicles', UserVehicleListView.as_view(), name='vehicle-list'),
]

urlpatterns += staticfiles_urlpatterns()
