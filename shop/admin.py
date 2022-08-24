from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models
# Register your models here.
from .models import Product,Contact,Orders,OrderUpdate

admin.site.register(Product)
admin.site.register(Orders)
admin.site.register(OrderUpdate)

class ContactAdmin(admin.ModelAdmin):
    formfield_overrides = {
    models.CharField: {"widget": TextInput(attrs={"size":"200"})},
     models.TextField: {"widget": Textarea(attrs={"rows":"30", "cols":200})}
}
admin.site.register(Contact, ContactAdmin)