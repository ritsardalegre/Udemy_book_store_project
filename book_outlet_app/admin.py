from django.contrib import admin

# Register your models here.
from .models import Book,Author,Address,Country #Import Model to register


@admin.register(Book) # Register Model using decorator
class BookAdmin(admin.ModelAdmin):
    # readonly_fields = ("slug",)
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("author", "rating",)
    list_display = ("title", "author",)

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "address",)


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    pass

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    pass
    

# admin.site.register(Book,BookAdmin) #registering the Book model