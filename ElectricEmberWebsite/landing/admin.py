from django.contrib import admin
from .models import UserInput

class UserInputAdmin(admin.ModelAdmin):
    class Meta:
        model = UserInput

admin.site.register(UserInput, UserInputAdmin)
