from django.contrib import admin
from .models import store_sale, bento, User, be_left
# Register your models here.

class bentoadmin(admin.ModelAdmin):
    list_display = ('name')
    fields = ('name')

class infoadmin(admin.ModelAdmin):
    readonly_fields = ('updated_at',)

admin.site.register(store_sale, infoadmin)
admin.site.register(bento)
admin.site.register(User)
admin.site.register(be_left, infoadmin)
