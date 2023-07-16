from django.shortcuts import render, HttpResponse
from .models import SaleProduct, Testimonial


# Create your views here.
def indexView(request):
    products = SaleProduct.objects.all()
    context = {
        "products":products
    }
    return render(request, 'shop/index.html', context=context)


def productDetail(request, prod_id):
    context = {}
    return render(request, 'shop/detail.html', context=context)
