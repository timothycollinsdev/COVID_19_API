from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'v1/all', DataView, basename='api-all')
urlpatterns = router.urls
