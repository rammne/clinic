from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('patient-form/', views.patient_form, name='patient-form'),
    path('patient-details/<int:pk>', views.patient_details, name='patient-details'),
    path('patient-form-update/<int:pk>', views.patient_form_update, name='patient-form-update'),
    path('patient-data/<int:pk>', views.patient_data, name='patient-data'),
    path('patient-permissions-form/<int:pk>', views.permissions_form, name='patient-permissions-form'),
    path('patient-permissions/<int:pk>', views.permissions_view, name='patient-permissions')
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
