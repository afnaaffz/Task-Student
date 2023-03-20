from django.contrib import admin

from new_app import models

# Register your models here.
admin.site.register(models.Login)
admin.site.register(models.StudentRegister)
admin.site.register(models.Complaint)
admin.site.register(models.Notification)




