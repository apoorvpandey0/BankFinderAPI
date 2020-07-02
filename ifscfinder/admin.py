from django.contrib import admin

from import_export.admin import ImportExportMixin
from import_export import resources

from .models import Bank
# Register your models here.
class BankResource(resources.ModelResource):

    class Meta:
        model = Bank

class BankAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display    = ("bank_name",'bank_id','district','state','branch','ifsc','city','address')
    search_fields   = ("bank_name",'bank_id','district','state','branch','ifsc','city','address')
    list_editable   = ()
    readonly_fields = ()
    filter_horizntal= ()
    list_filter     = ('state',)
    fieldsets       = ()

admin.site.register(Bank,BankAdmin)
