from django.contrib import admin
from .models import Message, Room

# Register your models here.


class MessageAdmin(admin.ModelAdmin):
    list_display = (
        "message",
        "timestamp",
    )
    list_filter = ("room",)
    search_fields = ("room",)


admin.site.register(Room)
admin.site.register(Message, MessageAdmin)