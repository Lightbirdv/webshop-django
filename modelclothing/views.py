from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import ClothingForm, CommentForm, SearchForm
from .models import Clothing, Comment


def all_clothing_list(request):
    all_clothes = Clothing.objects.all()
    context = {'all_the_clothes': all_clothes}
    print(context)
    return render(request, 'clothing-list.html', context)


def clothing_list_men(request):
    all_clothes = Clothing.objects.filter(sex='Male')
    context = {'all_the_clothes': all_clothes}
    print(context)
    return render(request, 'clothing-list-man.html', context)


def clothing_list_women(request):
    all_clothes = Clothing.objects.filter(sex='Female')
    context = {'all_the_clothes': all_clothes}
    print(context)
    return render(request, 'clothing-list-woman.html', context)


def filtered_clothing_list(request, filter):
    filtered_clothes = Clothing.objects.filter(type=filter)
    print(filtered_clothes)
    context = {'all_the_clothes': filtered_clothes}
    return render(request, 'clothing-list.html', context)


def filtered_clothing_list_men(request, filter):
    all_clothes = Clothing.objects.filter(sex='Male')
    filtered_clothes = all_clothes.filter(type=filter)
    print(filtered_clothes)
    context = {'all_the_clothes': filtered_clothes}
    return render(request, 'clothing-list.html', context)


def filtered_clothing_list_women(request, filter):
    all_clothes = Clothing.objects.filter(sex='Female')
    filtered_clothes = all_clothes.filter(type=filter)
    print(filtered_clothes)
    context = {'all_the_clothes': filtered_clothes}
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
    print(request.POST)
    if request.method == 'POST':
        search_string_name = request.POST['name']
        findings = Clothing.objects.filter(name__contains=search_string_name)

        search_string_description = request.POST['description']
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
    clothing = Clothing.objects.get(id=clothing_id)
    if clothing.already_commented(request.user.id):
        print('already commented')
        return redirect('clothing-detail', pk = clothing_id)
    text = request.POST['text']
    rating = request.POST['rating']
    form = CommentForm(request.POST)
    form.instance.text = text
    form.instance.rating = int(rating)
    form.instance.myuser = request.user
    form.instance.clothing = clothing
    if form.is_valid():
        form.save()
    else:
        print('form errors: ' + str(form.errors))
    return redirect('clothing-detail', pk = clothing_id)


def comment_update(request, commentid):
    comment = Comment.objects.get(id=commentid)
    clothing = Clothing.objects.get(id=comment.clothing_id)
    comments = Comment.objects.filter(clothing=clothing)
    form = CommentForm(instance=comment)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        print(form)
        if form.is_valid():
            print("form valid")
            form.save()
        else:
            print("form not valid")
            pass
        context = {'that_clothing': clothing,
               'comments_for_that_clothing': comments}
        return render(request, 'clothing-detail.html', context)

    context = {'form' : form,
                'comment':comment
    }
    return render(request, 'comment-edit.html', context) 


def comment_delete(request, commentid):
    comment = Comment.objects.filter(id=commentid)
    comment.delete()
    return redirect(request.META['HTTP_REFERER'])


def comment_report(request, **kwargs):
    comment_id = kwargs['pk']
    comment_to_be_reported = Comment.objects.get(id=comment_id)
    comment_to_be_reported.reported = True
    comment_to_be_reported.save()
    return redirect(request.META['HTTP_REFERER'])


def comment_usefulness_increment(request, commentid):
    comment = Comment.objects.filter(id=commentid)[0]
    print(comment.usefulness)
    comment.increment_usefulness()
    print(comment.usefulness)
    comment.save()
    return redirect(request.META['HTTP_REFERER'])