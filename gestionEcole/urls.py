
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('inscription/', include('inscription.urls')),
    path('admin/', admin.site.urls),
]
