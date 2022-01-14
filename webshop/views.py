from modelclothing.models import Clothing
from django.shortcuts import render


def home_view(request):
    trending = Clothing.objects.all().order_by('-timestamp')[:2]
    print(trending)
    context = {'trending_clothing': trending}
    return render(request, 'home.html', context)