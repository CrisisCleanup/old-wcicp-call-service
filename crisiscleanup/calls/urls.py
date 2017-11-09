from rest_framework import routers

from crisiscleanup.calls.api.call import CallViewSet
from crisiscleanup.calls.api.user import UserViewSet

router = routers.SimpleRouter()
router.register(r'calls', CallViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
]
