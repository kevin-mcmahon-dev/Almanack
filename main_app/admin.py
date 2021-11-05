from django.contrib import admin
from .models import Profile, City, Post, Comment
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Register your models here.

admin.site.register(Profile)
admin.site.register(City)
admin.site.register(Post)
admin.site.register(Comment)

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profile'

class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)

class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    list_filter = ('name',)
    prepopulated_fields = {'slug': ('name',) }

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.unregister(City)
admin.site.register(City, CityAdmin)

admin.site.unregister(Profile)
admin.site.register(Profile, ProfileAdmin)