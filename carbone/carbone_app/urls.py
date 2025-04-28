from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('downloads/<int:render_id>/', views.download_pdf, name='download_pdf'),
    path('generate/', views.home, name='generate'),  # <-- trailing slash!
]