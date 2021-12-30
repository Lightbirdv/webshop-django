from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import ClothingForm, CommentForm
from .models import Clothing, Comment


def all_clothing_list(request):
    all_clothes = Clothing.objects.all()
    context = {'all_the_clothes': all_clothes}
    print(context)
    return render(request, 'clothing-list.html', context)


# def clothing_list_filtered(request, **kwargs):
#     filter = kwargs['pk']
#     all_clothes_filtered = Clothing.objects.all().filter(type = filter);
#     context = {'all_the_clothing': all_clothes_filtered}
#     return render(request, 'clothing-list.html', context)


def clothing_detail(request, **kwargs):
    clothing_id = kwargs['pk']
    clothing = Clothing.objects.get(id=clothing_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        form.instance.user = request.user
        form.instance.clothing = clothing
        if form.is_valid():
            form.save()
        else:
            print(form.errors)

    comments = Comment.objects.filter(clothing=clothing)
    context = {'that_clothing': clothing,
               'comments_for_that_clothing': comments,
               'upvotes': clothing.get_upvotes_count(),
               'downvotes': clothing.get_downvotes_count(),
               'comment_form': CommentForm}
    return render(request, 'clothing-detail.html', context)


def clothing_create(request):
    if request.method == 'POST':
        create_clothing_form = ClothingForm(request.POST)
        create_clothing_form.instance.user = request.user
        if create_clothing_form.is_valid():
            create_clothing_form.save()
        else:
            pass
        return redirect('clothing-list')

    else: 
        create_clothing_form = ClothingForm()
        context = {'form': create_clothing_form}
        return render(request, 'clothing-create.html', context)


def clothing_delete(request, **kwargs):
    clothing_id = kwargs['pk']
    Clothing.objects.filter(id=clothing_id).delete()
    return redirect('clothing-list')

def vote(request, pk: str, up_or_down: str):
    clothing = Clothing.objects.get(id=int(pk))
    user = request.user
    clothing.vote(user, up_or_down)
    return redirect('clothing-detail', pk=pk)