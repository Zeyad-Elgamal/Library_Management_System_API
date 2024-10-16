from django.contrib import admin
from .models import Book, User

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn', 'published_date', 'available_copies')  # Use available_copies instead of copies_available

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'date_of_membership', 'is_active')  # Use is_active instead of active_status

admin.site.register(Book, BookAdmin)
admin.site.register(User, UserAdmin)
