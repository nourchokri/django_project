from django.contrib import admin # type: ignore
from .models import Participant,Reservations


class ReservationInline(admin.TabularInline):
    model = Reservations
    extra = 1  
    readonly_fields = ("reservation_date",)  
    autocomplete_fields = ('participant',)  


class ParticipantAdmin(admin.ModelAdmin):
    list_display = ("username","first_name","last_name","email","cin","participant_category", "created_at","updated_at",)
    search_fields = ("username", "first_name", "last_name", "email", "cin")
    list_per_page = 5
    ordering = ("created_at",)
    readonly_fields = ("created_at", "updated_at")  
    fieldsets = (
        ('Personal info', {
            'fields': ('username', 'first_name', 'last_name', 'email', 'cin', 'participant_category') 
        }),
        ('follow_up time', {
            'fields': ('created_at', 'updated_at')
        }),
    )
    inlines = [ReservationInline] 
    list_filter = ('participant_category',)
    list_editable = ('first_name', 'last_name')


# Register your models here.
admin.site.register(Participant,ParticipantAdmin)
admin.site.register(Reservations)