from django.contrib import admin
from .models import *
# Register your models here.

from import_export.admin import ImportExportModelAdmin

admin.site.register(Itdb  , ImportExportModelAdmin)
admin.site.register(Complaints)
admin.site.register(SolvedComplaints)
admin.site.register(UserModel)