from django.contrib import admin

# Imorts from local app(s)
from .models import Staff, Company, Empressa, Album, Call, Track, EmployeeSerializer

admin.site.register(Staff)
admin.site.register(Company)
admin.site.register(Empressa)
admin.site.register(Call)
admin.site.register(Album)
admin.site.register(Track)
admin.site.register(EmployeeSerializer)