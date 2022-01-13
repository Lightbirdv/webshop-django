from django.shortcuts import render, redirect
from modelclothing.forms import ClothingForm
from django.contrib.admin.views.decorators import staff_member_required
from modelclothing.models import Comment, Clothing

@staff_member_required(login_url='/useradmin/login/')
def clothing_create(request):
    if request.method == 'POST':
        create_clothing_form = ClothingForm(request.POST, request.FILES)
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


@staff_member_required(login_url='/useradmin/login/')
def clothing_update(request, pk):
    clothing = Clothing.objects.get(id=pk)
    form = ClothingForm(instance=clothing)

    if request.method == 'POST':
        form = ClothingForm(request.POST, instance=clothing)
        print(form)
        if form.is_valid():
            print("form valid")
            form.save()
        else:
            print("form not valid")
            pass
        return redirect('clothing-list')

    context = {'form': form}
    return render(request, 'clothing-create.html', context) 



@staff_member_required(login_url='/useradmin/login/')
def show_reported_comments(request):
    comments = Comment.objects.filter(reported=True)
    context = {'comment_list': comments}
    return render(request, 'comment-list.html', context)

@staff_member_required(login_url='/useradmin/login/')
def delete_reported_comments(request, pk):
    comment = Comment.objects.filter(id=pk)
    comment.delete()
    return redirect('comments-reported-show')

    