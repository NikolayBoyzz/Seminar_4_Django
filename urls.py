from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("1/", include("myapp.urls")),
    path("2/", include("myapp2.urls")),
    path("3/", include("myapp3.urls")),
]