from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from App import views

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),
    # Frontend
    path('', views.frontend, name="frontend"),
    # Backend
    path('backend/', views.backend, name="backend"),
    # Login/Logout
    path('login/', include('django.contrib.auth.urls')),

    path('', include('App.urls')),
]
urlpatterns = urlpatterns + \
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
