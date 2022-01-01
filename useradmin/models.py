from datetime import date, datetime
from django.contrib.auth.models import User
from django.db import models

def get_date_20_years_ago():
    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day
    return date(year - 20, month, day)

def get_myuser_from_user(user):
    myuser = None
    myuser_query_set = MyUser.objects.filter(user=user)
    if len(myuser_query_set) > 0:
        myuser = myuser_query_set.first()
    return myuser


class MyUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(default=get_date_20_years_ago())
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

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name + ' (' + str(self.date_of_birth) + ')'

