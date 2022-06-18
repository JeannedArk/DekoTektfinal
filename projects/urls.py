from django.urls import path 
from .import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [ 
    path('', views.home, name='home'),
    path('project/', views.work, name='work'),
    path('project/<slug:project_slug>/', views.work_details, name='work_details'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)