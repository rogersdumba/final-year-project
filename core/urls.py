from django.urls import path
from .views import indexView, productDetail


urlpatterns = [
    path("", indexView, name="index_page"),
    path("product/<prod_id>", productDetail, name="product_detail"),
]