from django.contrib import admin
from .models import ConnectFirstEvent, Gateway, Call, Language, User

admin_sites = [
    ConnectFirstEvent,
    Gateway,
    Call,
    Language,
    User
]

# Register your models here.
admin.site.register(admin_sites)