from django.contrib import admin

from .models import Manager,Store,StoreData,Sale,SaleAmount,Access,ConversionRate


class ManagerAdmin(admin.ModelAdmin):
    list_display    = [ "name" ]

class StoreAdmin(admin.ModelAdmin):
    list_display    = [ "id","name","date","manager","status" ]
    list_editable   = [ "manager","status" ]

class StoreDataAdmin(admin.ModelAdmin):
    list_display    = [ "store","date" ]

class SaleAdmin(admin.ModelAdmin):
    list_display    = [ "pc","phone","app","store_data" ]

    



class SaleAmountAdmin(admin.ModelAdmin):
    list_display    = [ "pc","phone","app","store_data" ]

class AccessAdmin(admin.ModelAdmin):
    list_display    = [ "pc","phone","app","store_data" ]

class ConversionRateAdmin(admin.ModelAdmin):
    list_display    = [ "pc","phone","app","store_data" ]



admin.site.register(Manager,       ManagerAdmin       )
admin.site.register(Store,         StoreAdmin         )
admin.site.register(StoreData,     StoreDataAdmin     )
admin.site.register(Sale,          SaleAdmin          )
admin.site.register(SaleAmount,    SaleAmountAdmin    )
admin.site.register(Access,        AccessAdmin        )
admin.site.register(ConversionRate,ConversionRateAdmin)


