from django.contrib import admin

from main.models import BookModel


@admin.register(BookModel)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'author',)

