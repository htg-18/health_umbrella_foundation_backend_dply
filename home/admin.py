from django.contrib import admin
from .models import disease_table, testimonial_table, video_table, key_value_table

class TestimonialAdmin(admin.ModelAdmin):
    list_filter = ('show',)

admin.site.register(disease_table)
admin.site.register(testimonial_table, TestimonialAdmin)
admin.site.register(video_table)
admin.site.register(key_value_table)
