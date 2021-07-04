from django.contrib import admin
from .models import Dog
from .models import User

# Register your models here.
admin.site.register(Dog)
admin.site.register(User)
