from django.contrib import admin
from chat.models import Message

# Register your models here.
class MessageAdmin(admin.ModelAdmin):
	list_display = ["room","username","content","date_added"]
	search_fields = ["room","username",'date_added']
	list_filter = ['room','date_added']

admin.site.register(Message, MessageAdmin)