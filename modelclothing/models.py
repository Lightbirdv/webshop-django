from django.db import models
from datetime import datetime
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

    SEX = [
        ('Male','male'),
        ('Female','female'),
        ('Unisex', 'unisex'),
    ]

    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=10, default=20.0)
    description = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    collection = models.CharField(max_length=50)
    timestamp = models.DateTimeField(default=datetime.now, blank=True)
    product_picture = models.ImageField(upload_to='product_pictures/', default= 'product_pictures/product-default.jpg')
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
    sex = models.CharField(max_length=6,
                            choices=SEX,
                            default='unisex'
                            )

    pdffile = models.FileField(upload_to='pdf_files', default= 'pdf_files/pdf-default.pdf')

    class Meta: 
        ordering = ['name', '-type']
        verbose_name = 'Clothing'
        verbose_name_plural = 'Clothes'

    def get_rating(self):
        clothing_votes = Comment.objects.filter(clothing_id = self.id)
        rating = 0
        for vote in clothing_votes:
            rating += vote.rating / len(clothing_votes)
        rating = round(rating,1)
        return str(rating)


    def __str__(self):
        return self.name + ' (' + self.collection + ')'


    def __repr__(self):
        return self.name + ' / ' + self.description + ' / ' + self.color + ' / ' + self.collection + ' / ' + self.size + ' / ' + self.type


    def clothing_details(self):
        return self.name + ' / ' + self.description + ' / ' + self.color + ' / ' + self.collection + ' / ' + self.size + ' / ' + self.type

class Comment(models.Model):
    text = models.TextField(max_length=500, blank=True)
    rating = models.IntegerField(default='5')
    timestamp = models.DateTimeField(auto_now_add=True)
    myuser = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    clothing = models.ForeignKey(Clothing, on_delete=models.CASCADE)
    reported = models.BooleanField(default=False)


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


    def is_reported(self):
        if self.reported == True:
            return True
        else:
            return False
