from django.urls import path

from user_access import views

app_name = 'user_access'

urlpatterns = [
    path('',views.HomeView.as_view(),name='home'),
    path('login/', views.UserLoginView.as_view(), name='login'),

    path('vehiclelist', views.VehicleListView.as_view(), name='vehiclelist'),
    path('create/', views.VehicleCreateView.as_view(), name='create'),
    path('detail/<int:pk>/', views.VehicleDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', views.VehicleUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.VehicleDeleteView.as_view(), name='delete'),


    path('user-signup/', views.UserSignupView.as_view(), name='usersignup'),
    path('admin-signup/', views.AdminSignupView.as_view(), name='adminsignup'),
    path('superuser-signup/', views.SuperAdminSignupView.as_view(), name='superadminsign'),


    path('logout/', views.UserLogoutView.as_view(), name='logout'),


]


