from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator


# Create your models here.
class UserProfile(User):
    seller_status = models.BooleanField(default=False)


class SaleCampaign(models.Model):
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(validators=[MinValueValidator])
    unit_price = models.PositiveIntegerField()
    pick_up_locations = models.TextField(help_text="input comma separated items")
    display_pictures = models.ImageField(upload_to="product_images")


class ProductSet(models.Model):
    campaign = models.ForeignKey(SaleCampaign, on_delete=models.CASCADE)
    size = models.PositiveIntegerField()

