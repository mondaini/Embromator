from django.contrib import admin
from generator.models import Fragment


class FragmentAdmin(admin.ModelAdmin):
    fields = ('text', 'column')
    list_display = ('text', 'column')
    list_filter = ('column',)

admin.site.register(Fragment, FragmentAdmin)