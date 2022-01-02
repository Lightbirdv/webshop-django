from datetime import date, datetime
from django.contrib.auth.models import AbstractUser
from django.db import models
from cart.models import Cart

def get_date_20_years_ago():
    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day
    return date(year - 20, month, day)


class MyUser(AbstractUser):

    USER_TYPES = [
        ('SU', 'superuser'),
        ('CS', 'customer service'),
        ('CU', 'customer'),
        ('BP', 'business partner'),
    ]

    date_of_birth = models.DateField(default=get_date_20_years_ago())
    type = models.CharField(max_length=2,
                            choices=USER_TYPES,
							default='CU',
                            )
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    def has_birthday_today(self):
        return_boolean = False

        now = datetime.now()
        today_month = now.month
        today_day = now.day

        user_month = self.date_of_birth.month
        user_day = self.date_of_birth.day

        if user_month == today_month and user_day == today_day:
            return_boolean = True
        return return_boolean

    def count_shopping_cart_items(self):
        count = 0
        if self.is_authenticated:
            shopping_carts = Cart.objects.filter(myuser=self)
            if shopping_carts:
                shopping_cart = shopping_carts.first()
                count = shopping_cart.get_number_of_items()

        return count

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name + ' (' + str(self.date_of_birth) + ')' + str(self.user_id)

