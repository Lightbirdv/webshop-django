from django.db import models

from decimal import Decimal
from django.conf import settings
from django.db import models
from django.utils import timezone


class Cart(models.Model):
    timestamp = models.DateTimeField(default=timezone.now)
    myuser = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               )

    def add_item(myuser, clothing, size):
        # Get existing shopping cart, or create a new one if none exists
        shopping_carts = Cart.objects.filter(myuser=myuser)
        if shopping_carts:
            shopping_cart = shopping_carts.first()
        else:
            shopping_cart = Cart.objects.create(myuser=myuser)

        product_picture = clothing.product_picture.url
        product_id = clothing.id
        product_collection = clothing.collection
        product_name = clothing.name
        product_color = clothing.color
        price = clothing.price
        csize = size
        print(product_collection + product_color)
        # check for existing item in shopping cart
        if CartItem.objects.filter(product_id=product_id).exists():
            item = CartItem.objects.filter(product_id=product_id)[0]
            if csize != item.size:
                CartItem.objects.create(product_picture=product_picture,
                                        product_id=product_id,
                                        product_collection=product_collection,
                                        product_name=product_name,
                                        product_color=product_color,
                                        price=price,
                                        size=csize,
                                        quantity=1,
                                        shopping_cart=shopping_cart,
                                        )
            else:
                item.quantity = item.quantity + 1
                item.save()

        else:
            CartItem.objects.create(product_picture=product_picture,
                                        product_id=product_id,
                                        product_collection=product_collection,
                                        product_name=product_name,
                                        product_color=product_color,
                                        price=price,
                                        size=csize,
                                        quantity=1,
                                        shopping_cart=shopping_cart,
                                        )

    def get_number_of_items(self):
        shopping_cart_items = CartItem.objects.filter(shopping_cart=self)
        number_of_items = 0
        for item in shopping_cart_items:
            number_of_items += item.quantity
        return number_of_items

    def get_total(self):
        total = Decimal(0.0)  # Default without Decimal() would be type float!
        shopping_cart_items = CartItem.objects.filter(shopping_cart=self)
        for item in shopping_cart_items:
            total += item.price * item.quantity
        return total


class CartItem(models.Model):
    product_picture = models.CharField(max_length=100, blank=True)
    product_id = models.IntegerField()
    product_collection = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    product_color = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    size = models.CharField(default='m', max_length=2)
    quantity = models.IntegerField(default=1)
    shopping_cart = models.ForeignKey(Cart,
                                      on_delete=models.CASCADE,
                                      )


class Payment(models.Model):
    credit_card_number = models.CharField(max_length=19)  # Format: 1234 5678 1234 5678
    expiry_date = models.CharField(max_length=7)  # Format: 10/2022
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    timestamp = models.DateTimeField(default=timezone.now)
    myuser = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               )
