from decimal import Decimal
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .forms import PaymentForm
from .models import Cart, CartItem
from modelclothing.models import Clothing, Comment
from modelclothing.forms import CommentForm


def show_shopping_cart(request):
    if request.method == 'POST':
        if 'empty' in request.POST:
            Cart.objects.get(myuser=request.user).delete()

            context = {'shopping_cart_is_empty': True,
                       'shopping_cart_items': None,
                       'amount': 0.0}
            return render(request, 'shopping-cart.html', context)

        elif 'pay' in request.POST:
            return redirect('shopping-cart-pay')

    else:  # request.method == 'GET'
        shopping_cart_is_empty = True
        shopping_cart_items = None
        total = Decimal(0.0)  # Default without Decimal() would be type float!

        myuser = request.user
        if myuser.is_authenticated:
            shopping_carts = Cart.objects.filter(myuser=myuser)
            if shopping_carts:
                shopping_cart = shopping_carts.first()
                shopping_cart_is_empty = False
                shopping_cart_items = CartItem.objects.filter(shopping_cart=shopping_cart)
                total = shopping_cart.get_total()

        context = {'shopping_cart_is_empty': shopping_cart_is_empty,
                   'shopping_cart_items': shopping_cart_items,
                   'total': total}
        return render(request, 'shopping-cart.html', context)


def add_shopping_cart(request, **kwargs):
    clothing_id = kwargs['pk']
    the_clothing_to_add = Clothing.objects.get(id=clothing_id)
    if request.method == 'POST':
        myuser = request.user
        Cart.add_item(myuser, the_clothing_to_add, request.POST['size'])
    comments = Comment.objects.filter(clothing=the_clothing_to_add)
    context = {'that_clothing': the_clothing_to_add,
               'comments_for_that_clothing': comments,
               'comment_form': CommentForm}
    return render(request, 'clothing-detail.html', context)


def remove_shopping_cart(request, **kwargs):
    item_id = kwargs['pk']
    item = CartItem.objects.get(id=item_id)
    item.delete()
    return redirect('shopping-cart-show')


@login_required(login_url='/useradmin/login/')
def pay(request):
    shopping_cart_is_empty = True
    paid = False
    form = None

    if request.method == 'POST':
        myuser = request.user
        form = PaymentForm(request.POST)
        form.instance.myuser = myuser
        if form.is_valid():
            form.save()
            paid = True

            # Empty the shopping cart
            Cart.objects.get(myuser=myuser).delete()
        else:
            print(form.errors)

    else:  # request.method == 'GET'
        shopping_carts = Cart.objects.filter(myuser=request.user)
        if shopping_carts:
            shopping_cart = shopping_carts.first()
            shopping_cart_is_empty = False
            form = PaymentForm(initial={'amount': shopping_cart.get_total()})

    context = {'shopping_cart_is_empty': shopping_cart_is_empty,
               'payment_form': form,
               'paid': paid,}
    return render(request, 'pay.html', context)
