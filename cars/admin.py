from django.contrib import admin
from django.utils.html import format_html
from cars.models import Car

# Register your models here.


class Caradmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(object.car_photo.url))
    thumbnail.short_description = 'pic'
    list_display = ('id','thumbnail','car_title', 'city', 'color', 'model',
                    'year', 'body_style', 'fuel_type', 'is_featured')
    list_display_links = ('id','thumbnail','car_title')
    list_editable=('is_featured',)
    search_fields=('id','car_title','model','body_style')
    list_filter=('city','model','fuel_type')

admin.site.register(Car, Caradmin)
