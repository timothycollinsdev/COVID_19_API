from django.contrib import admin

from .models import *


# Register your models here.
class CoronaCounrtyAdmin(admin.ModelAdmin):
	search_fields = ("country",)
	list_display = ("country", "total_cases", "new_cases", "total_deaths",
	                "new_deaths", "total_recovered", "active_cases", "serious_cases", "tot_cases", "track_it")
	list_filter = ("track_it",)
	ordering = ("total_cases",)


admin.site.register(CoronaCounrty, CoronaCounrtyAdmin)


class TrackCountryAdmin(admin.ModelAdmin):
	search_fields = ("country",)
	list_display = ("country", "total_cases", "new_cases", "total_deaths",
	                "new_deaths", "total_recovered", "active_cases", "serious_cases", "tot_cases")

admin.site.register(TrackCountry, TrackCountryAdmin)
