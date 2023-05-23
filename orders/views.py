from django.shortcuts import render
from django.http.response import JsonResponse

# Create your views here.
from basket.basket import Basket
from .models import Order, OrderItem

def add(request):
    basket=Basket(request)
    if request.POST.get('action') == 'post':
        user_id = request.user.id
        order_key = request.POST.get('order_key')
        baskettotal = basket.get_total_price()
        custName=request.POST.get('custName')
        custAdd=request.POST.get('custAdd')
        postCode=request.POST.get('postCode')
        

        if Order.objects.filter(order_key=order_key).exists():
             pass
        else:
            order = Order.objects.create(user_id=user_id, full_name=custName, address1=custAdd,
                                address2='add2', total_paid=baskettotal, order_key=order_key)
            order_id = order.pk

            for item in basket:
                OrderItem.objects.create(order_id=order_id, product=item['product'], price=item['price'], quantity=item['qty'])

        response = JsonResponse({'success': 'Return something'})
        return response


def payment_confirmation(data):
    Order.objects.filter(order_key=data).update(billing_status=True)


def user_orders(request):
    user_id = request.user.id
    orders = Order.objects.filter(user_id=user_id).filter(billing_status=True)
    return orders