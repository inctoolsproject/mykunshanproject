from django.contrib import admin

# Register your models here.
from .models import Flowchart, Flowchartprocess

class ProcessInline(admin.StackedInline):
    model = Flowchartprocess
    extra = 3


class FlowchartAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['part_name']}),
        ('Header', {'fields': ['mold_num','cust_name'], 'classes': ['collapse']}),
    ]
    inlines = [ProcessInline]

admin.site.register(Flowchart, FlowchartAdmin)
