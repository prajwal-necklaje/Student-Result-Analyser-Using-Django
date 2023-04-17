from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('analyse', views.dashboard_with_pivot, name='dashboard_with_pivot'),
    path('data', views.pivot_data, name='pivot_data'),
    path('detail', views.index, name='index'),
    path('add', views.add_order, name='add_order'),
    path('delete/<int:order_id>', views.delete_order, name='delete_order'),
    path('', views.home, name='home'),
    path('del', views.delte, name='delte'),
]
