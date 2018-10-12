from django.urls import path, re_path
from . import views

urlpatterns = [
    path('stock', views.stock),
    path('data', views.data),
    re_path(r'^search_s/$', views.search_s, name='search_s'),
    re_path(r'^return_s_data/$', views.return_s_data, name='return_s_data'),
    re_path(r'^update_data/$', views.update_data, name='update_data'),
]
