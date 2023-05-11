from django.contrib import admin

from .models import DataSet


@admin.register(DataSet)
class DataSetAdmin(admin.ModelAdmin):
    list_display = ['date', 'num_one', 'num_two', 'num_three',
                    'num_four', 'num_five', 'win']
