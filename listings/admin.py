from django.contrib import admin
from .models import Listing
# Register your models here.

class ListingAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'realtor', 'address', 'city','price','bedrooms','alan', 'is_published' )
  list_display_links = ('id','title')
admin.site.register(Listing, ListingAdmin)

