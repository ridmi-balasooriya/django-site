from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin', admin.site.urls),
    path('data_analyse/', include('data_analyse.urls')),
    path('', include('adoptions.urls')),
]
