from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Book

# Register your models here.

class BookResource(resources.ModelResource):
    class Meta:
        model = Book

@admin.register(Book)
class BookAdmin(ImportExportModelAdmin):
    resource_class = BookResource