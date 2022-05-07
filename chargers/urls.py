from django.urls import path
from .views import UserchargersDetailView,  UserChargersListView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('vehicles',UserChargersListView.as_view(), name='chargers-list'),
    path('vehicles/<int:pk>',  UserchargersDetailView.as_view(), name='chargers-detail'),
]

urlpatterns += staticfiles_urlpatterns()