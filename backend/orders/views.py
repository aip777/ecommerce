from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
# Create your views here.
from .forms import AddOrderForm, EditOrderForm, AddOrderItemForm
from products.models import Product
from .models import Order, OrderItem

from django.contrib.auth import get_user_model as user_model
User = user_model()
# @login_required()
def addOrderView(request):
    if request.method == 'POST':
        form = AddOrderForm(request.POST, request.FILES)
        order_item = AddOrderItemForm(request.POST, request.FILES)
        product_item = request.POST['product']
        if form.is_valid() and order_item.is_valid():
            form_obj = form.save(commit=False)
            form_obj.user = User.objects.get(pk=request.user.id)
           
             
            product_qy = Product.objects.filter(id=product_item)
            for obj in product_qy:
                if obj.current_stock>0:
                    print("Okay")
                else:
                    messages.success(request, "Product not available")
                    return HttpResponseRedirect("#") 
            form_obj.save()
            order_items = order_item.save(commit=False)
            order_items.order = form_obj
            order_items.save()
             
            messages.success(request, 'Successfully added')
            return redirect('order-list')
        else:
            messages.error(request, form.errors)
            return HttpResponseRedirect("#") 
    else:
        form = AddOrderForm()
        order_item = AddOrderItemForm()
        
    context = {
        'form': form,
        'order_item':order_item
    }
    return render(request, 'order/add-order.html', context)


# @login_required()
def orderlistView(request):
    order = Order.objects.all()
    order_item = OrderItem.objects.all()
    list_obj = list(zip(order, order_item))
    print(list_obj)
    context = {
        'order': list_obj
    }
    return render(request, 'order/order-list.html', context)

# @login_required()
def orderUpdateView(request, id):
    order = get_object_or_404(Order, id=id)
    if request.method == 'POST':
        form = EditOrderForm(request.POST, request.FILES, instance=order)

        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated')
            return redirect('order-list')
        else:
            messages.error(request, form.errors)
            return HttpResponseRedirect("#")
    else:
        form = EditOrderForm(instance=order)
    context = {
        'form': form,
    }
    return render(request, 'order/order-update.html', context)


# @login_required()
def deleteOrderView(request, id):
    order = get_object_or_404(Order, id=id)
    order.delete()
    messages.success(request, 'Successfully deleted')
    return redirect('order-list')


def orderDetailsView(request, id):
    order = get_object_or_404(Order, id=id)
    
    amount = {}
    list_li = []
   
    for obj in order.products.filter(order = order.id):
        list_li.append(obj.price)
    amount[order.id] = sum(list_li)
    list_li.clear()

    customer = Customer.objects.filter(id = order.customer.id )
    obj = amount.values()
    print(obj)
   
    print(order) 
    context = {
        'customer':customer,
        'obj':obj,
        'order': order
    }
    return render(request, 'order/order-details.html', context)