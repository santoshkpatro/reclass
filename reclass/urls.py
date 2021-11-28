from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('reclass.routes.auth.urls')),
    path('api/admin/', include('reclass.routes.admin.urls'))
]
