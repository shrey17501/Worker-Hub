from django.contrib import admin
from travello.models import Destination
from travello.models import Contact
from travello.models import Worker
from travello.models import Book

# Register your models here.

admin.site.register(Destination)
admin.site.register(Contact)
admin.site.register(Worker)
admin.site.register(Book)