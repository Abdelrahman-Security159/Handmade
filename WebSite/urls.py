from django.urls import path
from . import views

app_name = 'site'
urlpatterns = [
    path('index', views.index, name='index'),
    
    # Owner URLs
    path('owner/dashboard/', views.owner_dashboard, name='owner_dashboard'),
    path('owner/manage-services/', views.manage_services, name='manage_services'),
    path('owner/create-service/', views.create_service, name='create_service'),  # Add this line
    # path('owner/edit-service/<int:service_id>/', views.edit_service, name='edit_service'),  # Optional: If you have an edit view
    path('owner/delete-service/<int:service_id>/', views.delete_service, name='delete_service'),  # Optional: If you have a delete view

    # User URLs
    path('user/dashboard/', views.user_dashboard, name='user_dashboard'),
    path('user/view-shop/<int:shop_id>/', views.view_shop, name='view_shop'),
    path('user/purchase-service/<int:service_id>/', views.purchase_service, name='purchase_service'),
]