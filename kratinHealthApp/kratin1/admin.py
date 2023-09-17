from django.contrib import admin
from kratin1.models import HealthRecord,Food,CalorieIntake,Exercise,Activity

# Register your models here.
admin.site.register(HealthRecord)
admin.site.register(Food)
admin.site.register(CalorieIntake)
admin.site.register(Exercise)
admin.site.register(Activity)