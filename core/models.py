from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.shortcuts import reverse

# Create your models here.
class UserProfile(User):
    seller_status = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class SaleProduct(models.Model):
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="product_images")
    price = models.PositiveIntegerField(validators=[MinValueValidator(100)])
    in_stock = models.PositiveIntegerField(validators=[MinValueValidator(1)], default=1)
    pick_up_locations = models.TextField(help_text="input comma separated items", null=True, blank=True)
    variations = models.TextField(blank=True)
    special_features = models.TextField(blank=True, null=True)
    date_posted = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        product_link = reverse("product_detail", kwargs={"prod_id":self.id})
        return product_link


class Testimonial(models.Model):
    product = models.ForeignKey(SaleProduct, on_delete=models.CASCADE)
    message = models.TextField()
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.author) + ' testimonial on ' + str(self.product.name)
