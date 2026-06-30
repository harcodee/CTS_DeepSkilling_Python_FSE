from rest_framework.routers import DefaultRouter
from .views import (
    CourseViewSet,
    StudentViewSet,
    EnrollmentViewSet,
)

router = DefaultRouter()

router.register(r'courses', CourseViewSet, basename='courses')
router.register(r'students', StudentViewSet, basename='students')
router.register(r'enrollments', EnrollmentViewSet, basename='enrollments')

urlpatterns = router.urls