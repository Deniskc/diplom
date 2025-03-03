from django.contrib import admin

from users.models import User
from django.contrib.auth.models import Group


admin.site.unregister(Group)



# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = [
        'username',
        'first_name',
        'last_name',
        'surname',
        'birth_date',
        'phone_number',
        'email',
        'is_staff',  
    ]
    