from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('cms_put/', include('cms_put.urls')),
    path('calc/', include('calc.urls')),
    path('admin/', admin.site.urls),
]
