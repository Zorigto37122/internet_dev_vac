from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from core.views import SearchView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('search', SearchView.as_view(), name='search')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
