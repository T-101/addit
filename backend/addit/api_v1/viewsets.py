from django.db.models.functions import Lower
from rest_framework import viewsets
from rest_framework.response import Response

from addit.api_v1.serializers import QuoteSerializer
from addit.models import Quote


class QuoteViewSet(viewsets.ModelViewSet):
    serializer_class = QuoteSerializer
    queryset = Quote.visible.all()

    def list(self, *args, **kwargs):
        # Return nothing if query params are not up to speed
        filter_type = self.request.query_params.get("filter", None)
        query = self.request.query_params.get("q", None)
        if not filter_type or not query:
            self.queryset = Quote.objects.none()
            return super().list(*args, **kwargs)

        if filter_type.lower() == "topic":
            self.queryset = Quote().filter_by_topic(query)
        elif filter_type.lower() == "author":
            self.queryset = Quote().filter_by_handle(query)
        elif filter_type.lower() == "content":
            self.queryset = Quote().filter_by_content(query)
        else:
            self.queryset = Quote.objects.none()

        self.queryset = self.queryset.order_by(Lower("topic"))

        return super().list(*args, **kwargs)

    def retrieve_by_uuid(self, request, *args, **kwargs):
        # Override fetching quotes by db id. Just to throw a little curve ball.
        self.lookup_field = "uuid"
        return super().retrieve(request, *args, **kwargs)

    def retrieve_by_topic(self, request, *args, **kwargs):
        self.lookup_field = "topic"
        return super().retrieve(request, *args, **kwargs)


class RandomQuoteViewSet(viewsets.ModelViewSet):
    serializer_class = QuoteSerializer

    queryset = Quote.visible.all()

    def list(self, *args, **kwargs):
        query = self.request.query_params.get("q", None)
        quote = Quote().get_random_quote(query)
        serializer = self.get_serializer(quote)
        return Response(serializer.data)
