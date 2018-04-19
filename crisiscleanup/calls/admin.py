from django.contrib import admin
from .models import ConnectFirstEvent, Gateway, Call, Language, User, Caller

admin_sites = [
    ConnectFirstEvent,
    Gateway,
    Call,
    Language,
    User,
    Caller
]

# Register your models here.
admin.site.register(admin_sites)
