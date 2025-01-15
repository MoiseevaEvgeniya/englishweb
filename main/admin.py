from django.contrib import admin

# Register your models here.
from .models import *

class HeadAdmin(admin.ModelAdmin):
    list_display = ("title","time_create","time_update")
    list_display_links = ("title",)
    search_fields = ("title",)
class AboutAdmin(admin.ModelAdmin):
    list_display = ("about_title", "about_time_create", "about_time_update")
    list_display_links = ("about_title",)
    search_fields = ("about_title",)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("contact_content", "contact_time_create", "contact_time_update")
    list_display_links = ("contact_content",)

admin.site.register(Head_page,HeadAdmin)
admin.site.register(About_page,AboutAdmin)
admin.site.register(Contact_page,ContactAdmin)

admin.site.site_title="плнель"
admin.site.site_header="Админ-панель"
