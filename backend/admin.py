from django.contrib import admin

# Register your models here.

from .models import Lawyer
from .models import Client
from .models import Lawyercat
from .models import Case

admin.site.register(Lawyer)
admin.site.register(Client)
admin.site.register(Lawyercat)
admin.site.register(Case)
