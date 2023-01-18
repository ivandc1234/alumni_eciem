from django.contrib import admin
from django.urls import path, include 
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('table.urls')),
    path('', include('geo.urls')),
    path('', include('bolsa_laboral.urls')),
]


handler400 = 'table.views.handler400'
handler403 = 'table.views.handler403'
handler404 = 'table.views.handler404'
handler500 = 'table.views.handler500'

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
