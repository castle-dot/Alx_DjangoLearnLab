from django.contrib import admin
from .models import Book

# 1️⃣ Create a custom admin class for Book
class BookAdmin(admin.ModelAdmin):
    # 2️⃣ Columns to display in the list view
    list_display = ('title', 'author', 'publication_year')
    # 3️⃣ Sidebar filter
    list_filter = ('publication_year',)
    # 4️⃣ Search bar fields
    search_fields = ('title', 'author')

# 5️⃣ Register the Book model with the custom admin class
admin.site.register(Book, BookAdmin)
