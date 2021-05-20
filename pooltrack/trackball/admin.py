from django.contrib import admin

# Register your models here.
from trackball.models import pool_table , action_table

admin.site.register(pool_table)

admin.site.register(action_table)