from cart.forms import CartAddProductForm
from django.shortcuts import get_object_or_404, render

from .models import Product

# Create your views here.


class Shop:
    def shop(request):
        product = Product.objects.all()
        context = {"pr": product}
        return render(request, "shop/shop.html", context)

    def sortAction(self):
        product = Product.objects.filter(group="action")
        context = {"pr": product}
        return render(self, "shop/shop.html", context)

    def sortHorror(self):
        product = Product.objects.filter(group="horror")
        context = {"pr": product}
        return render(self, "shop/shop.html", context)

    def sortPuzzle(self):
        product = Product.objects.filter(group="puzzle")
        context = {"pr": product}
        return render(self, "shop/shop.html", context)

    def sortIndi(self):
        product = Product.objects.filter(group="indi")
        context = {"pr": product}
        return render(self, "shop/shop.html", context)

    def sortAdventure(self):
        product = Product.objects.filter(group="adventure")
        context = {"pr": product}
        return render(self, "shop/shop.html", context)

    def sortShooter(self):
        product = Product.objects.filter(group="shooter")
        context = {"pr": product}
        return render(self, "shop/shop.html", context)


# class ProductView:
def ProductView(request, id):
    product = get_object_or_404(Product, id=id)
    context = {"pr": product}
    return render(request, "shop/ProductView.html", context)


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    cart_product_form = CartAddProductForm()
    return render(
        request,
        "shop/ProductView.html",
        {"pr": product, "cart_product_form": cart_product_form},
    )
