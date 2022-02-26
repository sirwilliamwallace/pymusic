from django.contrib import admin

# Register your models here.
from .models import Ahang, CommentDb


@admin.register(Ahang)
class AhangManager(admin.ModelAdmin):
    list_display = ('author', 'ahang_esm', "isAgreed",)
    list_filter = ('publishDate', "isAgreed",)
    list_editable = ("isAgreed",)
    search_fields = ('author', 'ahang_esm',)
    actions = ["active_ahang", "deactivate_ahang", ]

    class Meta:
        model = Ahang

    def active_ahang(self, request, queryset):
        queryset.update(isAgreed=True)

    def deactivate_ahang(self, request, queryset):
        queryset.update(isAgreed=False)


@admin.register(CommentDb)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)
