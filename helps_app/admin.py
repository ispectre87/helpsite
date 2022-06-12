from django.contrib import admin

from .models import HelpRequest, City, Region

class RegionAdmin(admin.ModelAdmin):
    list_display = ('region_name',)
    search_fields = ('region_name',)

class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'city_name','region',)
    search_fields = ('city_name',)
    list_editable = ('region', 'city_name')

class HelpRequestAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'update', 'contacts', 'citi_name')
    list_filter = ('citi_name',)
admin.site.register(HelpRequest, HelpRequestAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Region, RegionAdmin)
