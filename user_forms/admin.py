from django.contrib import admin
from .models import join_us_table, share_experience_table

class JoinUsAdmin(admin.ModelAdmin):
    list_display = ("name","identity_verified")
    list_filter = ("identity_verified",)
    search_fields = ("name", "phone_number",)

class ShareExperienceAdmin(admin.ModelAdmin):
    list_display = ("name","disease","email_address","phone_number")
    search_fields = (
        "name",
        "pk",
        "city",
        "state",
        "country",
        "email_address",
        "phone_number",
        "disease",
        "pathies"
    )

admin.site.register(join_us_table, JoinUsAdmin)
admin.site.register(share_experience_table, ShareExperienceAdmin)
