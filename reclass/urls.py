import os
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('api/auth/', include('reclass.routes.auth.urls')),
    path('api/admin/', include('reclass.routes.admin.urls')),
    path('api/student/', include('reclass.routes.student.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if os.environ['DJANGO_SETTINGS_MODULE'] == 'reclass.settings.development':
    # from django.contrib import admin
    urlpatterns.append(path('admin/', admin.site.urls))
