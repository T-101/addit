from django.conf import settings
from django.urls import path, include
from rest_framework import routers

from addit.api_v1.viewsets import QuoteViewSet, RandomQuoteViewSet

router_class = routers.DefaultRouter if settings.DEBUG else routers.SimpleRouter


class OptionalSlashRouter(router_class):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.trailing_slash = "/?"


app_name = "api"

router = OptionalSlashRouter()

router.register('quotes', QuoteViewSet)
router.register('rexpl', RandomQuoteViewSet)

urlpatterns = [
    path('quotes/<uuid:uuid>/', QuoteViewSet.as_view({'get': 'retrieve_by_uuid'})),
    path('quotes/topic/<str:topic>/', QuoteViewSet.as_view({'get': 'retrieve_by_topic'})),
    path('', include(router.urls))
]
