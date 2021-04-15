from django.urls import path
from workblog.views import *


urlpatterns = [
    path("index/", workblog_index, name="index"),
    path("<int:id>/detail/", workblog_detail, name="detail"),
    path("create/", workblog_create, name="create"),
    path("<int:id>/update/", workblog_update, name="update"),
    path("<int:id>/delete/", workblog_delete, name="delete"),
    path("addtodb",workblog_addtodb,name="addtodb"),
    path("<int:id>/updated", workblog_updated, name="updated"),
    path("export/", workblog_export, name="export"),

]
