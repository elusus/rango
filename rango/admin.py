from django.contrib import admin
from rango.models import Category, Page, UserProfile


class PageAdmin(admin.ModelAdmin):
	list_display = ('category', 'title', 'url')

class PageInLine(admin.TabularInline):
	model = Page
	extra = 3

class CategoryAdmin(admin.ModelAdmin):
	fieldsets = [
		('Category',			{'fields': ['name']}),

	]
	inlines = [PageInLine]
	list_display = ('name', 'views', 'likes')

#admin.site.register(Category)
admin.site.register(Page, PageAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(UserProfile)