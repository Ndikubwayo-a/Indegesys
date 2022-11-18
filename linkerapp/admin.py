from django.contrib import admin
from .models import Team

admin.site.register(Team)


class TeamAdmin(admin.ModelAdmin):
    list_display = ('team_name', 'password')
    readonly_fields = ('team_id',)




