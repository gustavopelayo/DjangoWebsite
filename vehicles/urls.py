from django.urls import path
from .views import AddVehicleView, UserVehicleListView,  UserVehicleDetailView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path('vehicles/', UserVehicleListView.as_view(), name='vehicle-list'),
    path('vehicles/<int:pk>/',  views.UserVehicleDetailView , name='vehicle-detail'),
    path('vehicles/add/', AddVehicleView.as_view() , name='vehicle-form'),

]

urlpatterns += staticfiles_urlpatterns()
