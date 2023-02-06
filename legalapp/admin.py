from django.contrib import admin

from .models import Client, Lawyer


class ClientAdmin(admin.ModelAdmin):
    list_display = ["firstname", "lastname", "request", "description", "email", "phone"]
    search_fields = ["firstname", "lastname", "email"]
    list_per_page = 10


admin.site.register(Client, ClientAdmin)

class LawyerAdmin(admin.ModelAdmin):
    list_display = ["Company", "FirstName", "Category", "Gender", "Experience", "Email", "Phone"]
    search_fields = ["Company", "FirstName", "Category", "Email"]
    list_per_page = 10


admin.site.register(Lawyer, LawyerAdmin)
