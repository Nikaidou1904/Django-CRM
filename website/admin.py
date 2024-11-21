from django.contrib import admin
from .models import Record
from .models import Airline
from .models import Backpack

admin.site.register(Record)
admin.site.register(Airline)
admin.site.register(Backpack)