from django.contrib import admin
from django.urls import path
from rest_framework.routers import SimpleRouter
from rest_framework_nested import routers
from Ressources.views import VehiculeViewSet
from Entreprise.views import AccueilEntreprises
from Ressources.views import ImportEnginView
from Preventive.views import CompteurViews, CreateSuiviEP, ListSuiviEP, UpSuiviEP, DeleteSuiviEP, ImportSuiviEP


router = routers.DefaultRouter()


router.register("engins", VehiculeViewSet, basename="engins")
# router.register("compteur", CompteurViews, basename="compteur")

engin_router = routers.NestedSimpleRouter(router, "engins", lookup='engin')

engin_router.register("compteur", CompteurViews, basename='engin-compteur')

urlpatterns = [
    path('', AccueilEntreprises.as_view(), name="accueil"),
    path('import-engins', ImportEnginView.as_view(), name="import-engins"),
    path('admin/', admin.site.urls),


    path('create-suiviep', CreateSuiviEP.as_view(), name="create-suiviep"),
    path('list-suiviep', ListSuiviEP.as_view(), name="list-suiviep"),
    path('update-suiviep/<str:pk>', UpSuiviEP.as_view(), name="update-suiviep"),
    path('delete-suiviep/<str:pk>', DeleteSuiviEP.as_view(), name="delete-suiviep"),
    path('import-suiviep', ImportSuiviEP.as_view(), name="import-suiviep"),


    # path('create-compteur', CompteurViews.as_view(), name="create-compteur"),


] + router.urls + engin_router.urls

