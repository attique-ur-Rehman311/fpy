from django.urls import path
from . import views
from django.contrib import admin 

urlpatterns = [

path('admin/',admin.site.urls),
path('', views.login_view, name='login'),
path('register/', views.register_view, name='register'),

path('dashboard/', views.dashboard_view, name='dashboard'),
path('dashboard-data/', views.dashboard_data, name='dashboard_data'),
path('filter-options/', views.filter_options, name='filter_options'),

path('pridiction/', views.prediction_view, name='pridiction'),
path('predict-price/', views.predict_price, name='predict_price'),
path('report/', views.report_view, name='report'),

# ✅ ADD THIS
path('logout/', views.logout_view, name='logout'),
    
]

