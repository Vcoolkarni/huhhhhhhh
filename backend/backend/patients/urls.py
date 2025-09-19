from rest_framework.routers import DefaultRouter
from .views import PatientViewSet, DoctorViewSet

router = DefaultRouter()
router.register(r'patients', PatientViewSet)
router.register(r'doctors', DoctorViewSet)

urlpatterns = router.urls