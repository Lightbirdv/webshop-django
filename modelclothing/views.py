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

    comments = Comment.objects.filter(clothing=clothing)
    context = {'that_clothing': clothing,
               'comments_for_that_clothing': comments,
            #    'rating': clothing.get_rating(),
            #    'comment_form': CommentForm
                }
    return render(request, 'clothing-detail.html', context)


def clothing_delete(request, **kwargs):
    clothing_id = kwargs['pk']
    Clothing.objects.filter(id=clothing_id).delete()
    return redirect('clothing-list')


def clothing_search(request):
    if request.method == 'POST':
        search_string_name = request.POST['name']
        findings = Clothing.objects.filter(name__contains=search_string_name)

        search_string_description = request.Post['description']
        if search_string_description:
            findings = findings.filter(description__contains=search_string_description)

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


def comment_create(request, **kwargs):
    clothing_id = kwargs['pk']
    text = request.POST['text']
    rating = request.POST['rating']
    clothing = Clothing.objects.get(id=clothing_id)
    print('clothing: ' + str(clothing))
    print('clothing_id: ' + str(clothing_id))
    print('text: ' + str(text))
    print('rating: ' + str(rating))
    form = CommentForm()
    form.instance.text = text
    form.instance.rating = int(rating)
    form.instance.myuser = request.user
    form.instance.clothing = clothing
    print('form instance: ' + str(form.instance))
    print('form: ' + str(form))
    if form.is_valid():
        print("valid")
        form.save()
    else:
        print("not valid")
        print('form errors: ' + str(form.errors))
    return redirect('clothing-detail', pk = clothing_id)


def comment_report(request, **kwargs):
    comment_id = kwargs['pk']
    comment_to_be_reported = Comment.objects.get(id=comment_id)
    comment_to_be_reported.reported = True
    comment_to_be_reported.save()
    return redirect(request.META['HTTP_REFERER'])