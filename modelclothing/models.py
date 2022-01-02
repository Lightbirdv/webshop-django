from django.db import models

# Create your models here.
from django.db import models
from datetime import date
from useradmin.models import MyUser
from django.conf import settings 

# Create your models here.
class Clothing(models.Model):
    SIZE = [
        ('XS', 'xs'),
        ('S', 's'),
        ('M', 'm'),
        ('L', 'l'),
        ('XL', 'xl'),
        ('XXL', 'xxl')
    ]

    TYPE = [
        ('Jackets','jackets'),
        ('T-Shirts','t-shirts'),
        ('Shirts', 'shirts'),
        ('Pants', 'pants'),
        ('Jeans', 'jeans'),
        ('Pullovers', 'pullovers'),
        ('Hoodies', 'hoodies'),
        ('Shoes', 'shoes'),
        ('Basics', 'basics'),
        ('Accessoires', 'accessoires'),
        ('Underwear', 'underwear'),
        ('Dresses', 'dresses'),
        ('Suits', 'suits'),
    ]

    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=10, default=20.0)
    description = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    collection = models.CharField(max_length=50)
    size = models.CharField(max_length=3,
                            choices=SIZE,
                            )

    type = models.CharField(max_length=12,
                            choices=TYPE,
                            )

    myuser = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE,
                              related_name='clothing_created_by',
                              related_query_name='clothing_created_by',
                              )

    # pdffile = models.FileField(upload_to="static files/")

    class Meta: 
        ordering = ['name', '-type']
        verbose_name = 'Clothing'
        verbose_name_plural = 'Clothes'

    def get_upvotes(self):
        upvotes = Vote.objects.filter(up_or_down='U',
                                      clothing=self)
        return upvotes

    def get_upvotes_count(self):
        return len(self.get_upvotes())

    def get_downvotes(self):
        downvotes = Vote.objects.filter(up_or_down='D',
                                        clothing=self)
        return downvotes

    def get_downvotes_count(self):
        return len(self.get_downvotes())

    def vote(self, myuser, up_or_down):
        U_or_D = 'U'
        if up_or_down == 'down':
            U_or_D = 'D'
        vote = Vote.objects.create(up_or_down=U_or_D,
                                   myuser=myuser,
                                   clothing=self
                                   )

    def __str__(self):
        return self.name + ' (' + self.collection + ')'

    def __repr__(self):
        return self.name + ' / ' + self.description + ' / ' + self.color + ' / ' + self.collection + ' / ' + self.size + ' / ' + self.type

    def clothing_details(self):
        return self.name + ' / ' + self.description + ' / ' + self.color + ' / ' + self.collection + ' / ' + self.size + ' / ' + self.type

class Comment(models.Model):
    text = models.TextField(max_length=500)
    timestamp = models.DateTimeField(auto_now_add=True)
    myuser = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    clothing = models.ForeignKey(Clothing, on_delete=models.CASCADE)

    class Meta:
        ordering = ['timestamp']
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def get_comment_prefix(self):
        if len(self.text) > 50:
            return self.text[:50] + '...'
        else:
            return self.text

    def __str__(self):
        return self.get_comment_prefix() + ' (' + self.myuser.username + ')'

    def __repr__(self):
        return self.get_comment_prefix() + ' (' + self.myuser.username + ' / ' + str(self.timestamp) + ')'


class Vote(models.Model):
    VOTE_TYPES = [
        ('U', 'up'),
        ('D', 'down'),
    ]

    up_or_down = models.CharField(max_length=1,
                                  choices=VOTE_TYPES,
                                 )
    timestamp = models.DateTimeField(auto_now_add=True)
    myuser = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    clothing = models.ForeignKey(Clothing, on_delete=models.CASCADE)

    def __str__(self):
        return self.up_or_down + ' on ' + self.clothing.name + ' by ' + self.myuser.username