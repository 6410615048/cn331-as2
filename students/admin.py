from django.contrib import admin
from .models import Course, Profile

class CourseAdmin(admin.ModelAdmin):
    list_display = ("code", "course_name", "seat", "status")

class ProfileAdmin(admin.ModelAdmin):
    filter_horizontal = ["courses"]
    
admin.site.register(Course, CourseAdmin)
admin.site.register(Profile, ProfileAdmin)