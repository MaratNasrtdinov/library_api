from django.contrib import admin
from .models import UserModel

@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'id', 'email')
    fields = ('id', 'username', 'email', 'date_joined')
    readonly_fields = ('id', 'date_joined')



