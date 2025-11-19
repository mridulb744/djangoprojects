from multiprocessing.resource_tracker import register

from django.contrib import admin
from app1.models import Customuser
# Register your models here.

admin.site.register(Customuser)
