from django.contrib import admin


from .models import PadLock

class PadLockAdmin(admin.ModelAdmin):
    model = PadLock
    list_display_links=['lock_nature',]
    list_display=['lock_nature','active_state']
    list_editable=['active_state']


admin.site.register(PadLock,PadLockAdmin)