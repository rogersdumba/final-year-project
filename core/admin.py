from django.contrib import admin
from .models import SaleProduct, UserProfile, Testimonial

# Register your models here.
admin.site.register(SaleProduct)
admin.site.register(UserProfile)
admin.site.register(Testimonial)
