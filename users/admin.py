from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


from .forms import CustomUserCreationForm
from .models import CustomUser




class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    model = CustomUser
    list_display=['email','username','age','is_staff','lock_status','lock_count','user_locked_with','user_is_reciever','user_is_sender','lock_exist','lock_published']
    list_editable=['username','lock_status','lock_count','user_locked_with','user_is_reciever','user_is_sender','lock_exist','lock_published']

admin.site.register(CustomUser,CustomUserAdmin)
