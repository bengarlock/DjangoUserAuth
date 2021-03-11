from rest_framework import routers
from .views import PostViewSet

router = routers.DefaultRouter()
router.register('api/v1/posts', PostViewSet, 'posts')


urlpatterns = router.urls

