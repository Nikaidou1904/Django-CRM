from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    #path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    # Airline Links
    path('airline/', views.airline_record, name='airline'),
    path('info_airline/<int:pk>', views.info_airline, name='info_airline'),
    path('delete_airline/<int:pk>', views.delete_airline, name='delete_airline'),
    path('add_airline/', views.add_airline, name='add_airline'),
    path('update_airline/<int:pk>', views.update_airline, name='update_airline'),
    # Backpack Links
    path('backpack/', views.backpack_record, name='backpack'),
    path('info_backpack/<int:pk>', views.info_backpack, name='info_backpack'),
    path('delete_backpack/<int:pk>', views.delete_backpack, name='delete_backpack'),
    path('add_backpack/', views.add_backpack, name='add_backpack'),
    path('update_backpack/<int:pk>', views.update_backpack, name='update_backpack'),

]