from django.contrib import admin

# Register your models here.

from .models import Lawyer
from .models import Client
from .models import Lawyercat
from .models import Case
from .models import Register

admin.site.register(Lawyer)
admin.site.register(Client)
admin.site.register(Lawyercat)
admin.site.register(Case)


class RegisterAdmin(admin.ModelAdmin):
    list_display = ["firstname", "lastname", "email"]
    search_fields = ["firstname", "lastname", "email"]
    list_per_page = 10


admin.site.register(Register, RegisterAdmin)
