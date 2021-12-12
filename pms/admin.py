from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, AdminHOD, Staffs, Students, Domains, Projects,StudentFeedback
# Register your models here.
class UserModel(UserAdmin):
    pass


admin.site.register(CustomUser, UserModel)
admin.site.register(AdminHOD)
admin.site.register(Staffs)
admin.site.register(Domains)
admin.site.register(Projects)
admin.site.register(Students)
admin.site.register(StudentFeedback)