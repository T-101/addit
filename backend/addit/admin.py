from django.contrib import admin

from addit.models import Quote


class QuoteAdmin(admin.ModelAdmin):
    list_display = ['topic', 'slug', 'handle', 'content', 'time_added', 'is_visible']
    search_fields = ['topic', 'handle', 'content']
    readonly_fields = ['slug', 'uuid']


admin.site.register(Quote, QuoteAdmin)
