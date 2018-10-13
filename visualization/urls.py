from django.urls import path, re_path
from . import views

urlpatterns = [
    path('stock', views.stock),
    path('data_update', views.data_update),
    path('data_load', views.data_load),
    re_path(r'^search_s/$', views.search_s, name='search_s'),
    re_path(r'^return_data/$', views.return_data, name='return_data'),
    re_path(r'^update_data/$', views.update_data, name='update_data'),
    re_path(r'^load_data/$', views.load_data, name='load_data'),
    re_path(r'^load_data2/$', views.load_data2, name='load_data2'),
]
