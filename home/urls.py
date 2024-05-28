from django.urls import path , include
from home import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter ()
router.register ('view' , views.Clinic_view , basename='view')

urlpatterns = [
    path ('' , include (router.urls)),
]
