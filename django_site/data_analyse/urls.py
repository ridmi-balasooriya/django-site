from django.urls import path
from . import views

urlpatterns = [
    path('', views.data_home, name='data_home'),
    path('analyse_data', views.analyse_data, name='analyse_data'),
    path('check_posibility', views.check_posibility, name='check_posibility'),
    path('individual_posibility/<int:data_id>/',
         views.individual_posibility, name='individual_posibility'),
    path('add_new_data', views.add_new_data, name='add_new_data'),
    path('ajax_view', views.ajax_view, name='ajax_view')
]
