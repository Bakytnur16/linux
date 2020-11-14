from django.contrib import admin
#from django.contrib.auth.models import User
from .models import Author, Genre, Book, BookInstance

#admin.site.unregister(User)
#admin.site.register(User, MyUserAdmin)

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(BookInstance)

# admin.site.register(Author)
# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    pass

# Register the admin class with the associated model
#admin.site.register(Author, AuthorAdmin)

#admin.site.register(Book)
#admin.site.register(BookInstance)
# Register the Admin classes for Book using the decorator

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass

# Register the Admin classes for BookInstance using the decorator

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')
    
    fieldsets = (
        (None, {
            'fields': ('book','imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back','borrower')
        }),
    )



class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')

class BookAdmin(admin.ModelAdmin):
   list_display = ('title', 'author', 'display_genre')