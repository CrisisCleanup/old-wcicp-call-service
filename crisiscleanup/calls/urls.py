from rest_framework import routers

from crisiscleanup.calls.api.call import CallViewSet

router = routers.SimpleRouter()
router.register(r'calls', CallViewSet)

urlpatterns = [
]
