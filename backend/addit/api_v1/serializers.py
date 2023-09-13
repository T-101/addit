from rest_framework import serializers

from addit.models import Quote


class QuoteSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        export = kwargs.pop("export", False)
        super().__init__(*args, **kwargs)
        if not export:
            self.fields.pop('is_visible')

    class Meta:
        model = Quote
        fields = ['time_added', 'handle', 'topic', 'content', 'uuid', 'is_visible']

