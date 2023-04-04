from django.contrib import admin
from .models import disease_table, testimonial_table, video_table, key_value_table


class TestimonialAdmin(admin.ModelAdmin):
    list_filter = ('show',)
    list_display = ('heading', 'text', 'name', 'location')

class DiseaseAdmin(admin.ModelAdmin):
    list_display = ('disease',)

class VideoAdmin(admin.ModelAdmin):
    list_display = ('heading', 'image', 'ytplaylist_link')

class Key_valueAdmin(admin.ModelAdmin):
    list_display = ('key', 'value')

admin.site.register(disease_table, DiseaseAdmin)
admin.site.register(testimonial_table, TestimonialAdmin)
admin.site.register(video_table, VideoAdmin)
admin.site.register(key_value_table, Key_valueAdmin)
