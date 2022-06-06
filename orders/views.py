import logging

from cart.cart import Cart
from django.shortcuts import render

from .forms import OrderCreateForm
from .models import OrderItem
from .tasks import order_created

logger = logging.getLogger(__name__)


def order_create(request):
    cart = Cart(request)
    if request.method == "POST":
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item["product"],
                    price=item["price"],
                    quantity=item["quantity"],
                )
            # очистка корзины
            cart.clear()
            order_created.delay(order.id)
            logger.info(
                f"The order : {order.id} was succesfully added, of user {request.user}"
            )
            return render(request, "main/index.html", {"order": order})
    else:
        form = OrderCreateForm
    return render(request, "orders/create.html", {"cart": cart, "form": form})
