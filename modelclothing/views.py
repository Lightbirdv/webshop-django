from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import ClothingForm, CommentForm, SearchForm
from .models import Clothing, Comment


def all_clothing_list(request):
    all_clothes = Clothing.objects.all()
    context = {'all_the_clothes': all_clothes}
    print(context)
    return render(request, 'clothing-list.html', context)


def clothing_detail(request, **kwargs):
    clothing_id = kwargs['pk']
    clothing = Clothing.objects.get(id=clothing_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        form.instance.myuser = request.user
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
        create_clothing_form.instance.myuser = request.user
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


def clothing_search(request):
    if request.method == 'POST':
        search_string = request.POST['name']
        findings = Clothing.objects.filter(name__contains=search_string)

        form_in_function_based_view = SearchForm()
        context = {'form': form_in_function_based_view,
                   'findings': findings,
                   'show_results': True}
        return render(request, 'clothing-search.html', context)

    else:
        form_in_function_based_view = SearchForm()
        context = {'form': form_in_function_based_view,
                   'show_results': False}
        return render(request, 'clothing-search.html', context)


def vote(request, pk: str, up_or_down: str):
    clothing = Clothing.objects.get(id=int(pk))
    myuser = request.user
    clothing.vote(myuser, up_or_down)
    return redirect('clothing-detail', pk=pk)