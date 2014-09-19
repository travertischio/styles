from django.contrib import admin
from styles.models import BeerStyle

class StyleAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['name']}),
	('Information', {'fields': ['ibu', 'srm', 'abv', 'country', 'similarity', 'brands']}),
	]
	list_display = ('name', 'ibu', 'srm', 'abv', 'country', 'similarity', 'brands')
	search_fields = ['name']

admin.site.register(BeerStyle, StyleAdmin)