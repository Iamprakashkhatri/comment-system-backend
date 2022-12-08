from django.contrib import admin
from django.apps import apps

app = apps.get_app_config('user')

for model_name, model in app.models.items():
    # create a custom admin class
    class PostAdmin(admin.ModelAdmin):
        list_display = [field.name for field in model._meta.fields]
        
    try:
        admin.site.register(model, PostAdmin)
    except:
        pass