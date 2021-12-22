from django.contrib import admin
from .models import EmailEventDatabase,Ip
# Register your models here.
class  IpInline(admin.TabularInline):
    model = Ip
class EmailEventDatabaseAdmin(admin.ModelAdmin):
    list_display    =   ['id','email','no_of_opening','last_opened_time','last_used_ip','last_location']
    inlines         =   [IpInline]
admin.site.register(EmailEventDatabase,EmailEventDatabaseAdmin)
class IpAdmin(admin.ModelAdmin):
    list_display    =   ['email_event','ip','location']
admin.site.register(Ip,IpAdmin)

