from django.contrib import admin
from .models import Workchart

# Register your models here.


class WorkchartAdmin(admin.ModelAdmin):
    # admin panelinde gözükenler
    list_display = ["project","publishingdate"]
    # admin panelinde tıklandığında gitme
    list_display_links = ["publishingdate"]
    # admin panelinde filtreleme
    list_filter = ["publishingdate"]
    #admin panelinde arama
    search_fields = ["project"]
    #admin panelinde direkt editleme
    list_editable = ["project"]

    class Meta:
        model = Workchart



admin.site.register(Workchart, WorkchartAdmin)