from django.contrib import admin
from . import models
from django.core.exceptions import ValidationError
from django.contrib import messages


class VendorAdmin(admin.ModelAdmin):
    search_fields = ["full_name","mobile"]
    list_display=['full_name','address','mobile','photo']
admin.site.register(models.Vendor,VendorAdmin)

admin.site.register(models.Unit)
admin.site.register(models.Product)


class PurchaseAdmin(admin.ModelAdmin):
    list_display=['id','product','vendor','qty','price','total_amt','pur_date']
admin.site.register(models.Purchase,PurchaseAdmin)

class SaleAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        try:
            obj.save()
        except ValidationError as e:
            self.message_user(request, e.message, level=messages.ERROR)

    list_display=['id','product','qty','price','total_amt','sale_date']
admin.site.register(models.Sale,SaleAdmin)

class InventoryAdmin(admin.ModelAdmin):
    search_fields = ["product__title"]
    list_display=['product','pur_qty','sale_qty','total_bal_qty']
admin.site.register(models.Inventory,InventoryAdmin)
