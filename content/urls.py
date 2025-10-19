from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('subject/<slug:slug>/', views.subject_detail, name='subject_detail'),
    path('assistant/', views.assistant_page, name='assistant_page'),
    path('assistant/ask/', views.assistant_ask, name='assistant_ask'),
    path('admin/upload/', views.admin_upload_page, name='admin_upload_page'),
    path('admin/upload/submit/', views.admin_upload_submit, name='admin_upload_submit'),
]
