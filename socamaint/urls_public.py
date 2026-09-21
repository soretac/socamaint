from django.contrib import admin
from django.urls import path
from rest_framework.routers import SimpleRouter
from Client.views import  ClientViewSet
from django.conf import settings
from django.conf.urls.static import static
from Entreprise.views import Valid


router = SimpleRouter()
router.register('client', ClientViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('validation/', Valid.as_view(), name="validation"),
    
] + router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
