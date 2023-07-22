from django.contrib import admin
from .models import (
    disease_table,
    pathy_table,
    summary_table,
    data_table,
    source_table,
    case_table,
    sex_table,
    book_table,
    whatsapp_table,
)


class DiseaseAdmin(admin.ModelAdmin):
    list_filter = ("show",)


class PathyAdmin(admin.ModelAdmin):
    list_filter = ("show",)


class DataAdmin(admin.ModelAdmin):
    list_filter = ("show",)


class SourceAdmin(admin.ModelAdmin):
    list_filter = ("show",)


class CaseAdmin(admin.ModelAdmin):
    list_filter = ("show",)


class SexAdmin(admin.ModelAdmin):
    list_filter = ("show",)


class BookAdmin(admin.ModelAdmin):
    list_filter = ("show",)


class WhatsappAdmin(admin.ModelAdmin):
    list_filter = ("show",)


admin.site.register(disease_table, DiseaseAdmin)
admin.site.register(pathy_table, PathyAdmin)
admin.site.register(summary_table)
admin.site.register(data_table, DataAdmin)
admin.site.register(source_table, SourceAdmin)
admin.site.register(case_table, CaseAdmin)
admin.site.register(sex_table, SexAdmin)
admin.site.register(book_table, BookAdmin)
admin.site.register(whatsapp_table, WhatsappAdmin)
