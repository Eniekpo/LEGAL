from django.contrib import admin
from django.utils.html import format_html
# Register your models here.
from django.contrib import admin

from .models import Client, Lawyer, Cases


class ClientAdmin(admin.ModelAdmin):
    list_display = ["firstname", "lastname", "case_type", "email", "phone"]
    search_fields = ["firstname", "lastname", "email"]
    list_per_page = 10


admin.site.register(Client, ClientAdmin)


class LawyerAdmin(admin.ModelAdmin):
    list_display = ["Firm", "FirstName", "Lawyer_type", "Gender", "Experience", "Email", "Phone"]
    search_fields = ["Company", "FirstName", "Email"]
    list_per_page = 10


admin.site.register(Lawyer, LawyerAdmin)


class CasesAdmin(admin.ModelAdmin):
    list_filter = ['situation']
    list_display = ["case_id", "case_type", 'client',
                    "lawyer", "created_at", "status", "_"]
    search_fields = ["case_id", "case_type", 'client', "lawyer", "situation" ]
    list_per_page = 10

    # Function to change the icon
    def _(self, obj):
        if obj.situation == 'Completed':
            return True
        elif obj.situation == 'InProgress':
            return None
        else:
            return False
    _.boolean = True

    # Function to color the text

    def status(self, obj):
        if obj.situation == 'Completed':
            color = '#28a745'
        elif obj.situation == 'InProgress':
            color = '#fea95e'
        else:
            color = 'red'
        return format_html('<strong><p style="color: {}">{}</p></strong>'.format(color, obj.situation))

    status.allow_tags = True


admin.site.register(Cases, CasesAdmin)
