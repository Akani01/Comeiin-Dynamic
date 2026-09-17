from django.contrib import admin
from .models import QuoteRequest, QuoteItem


class QuoteItemInline(admin.TabularInline):
    model = QuoteItem
    extra = 0


@admin.register(QuoteRequest)
class QuoteRequestAdmin(admin.ModelAdmin):
    list_display = ('reference', 'name', 'email', 'company', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('reference', 'name', 'email', 'company')
    readonly_fields = ('reference', 'created_at')
    inlines = [QuoteItemInline]
    list_editable = ('status',)