from django.contrib import admin
from .models import Contact

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
	list_display = ("first_name", "email_id", "phone_number", "favorite",)

admin.site.register(Contact, ContactAdmin)
