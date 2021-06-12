from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import Createform
from django.contrib import messages



@login_required
def editpost(request, id):
        obj= get_object_or_404(Post, id=id)
        
        form = Createform(request.POST or None, instance= obj)
        context= {'form': form}

        if form.is_valid():
                obj= form.save(commit= False)

                obj.save()

                messages.success(request, "You successfully updated the post")

                context= {'form': form}

                return render(request, 'posts/edit.html', context)

        else:
                context= {'form': form,
                           'error': 'The form was not updated successfully. Please enter in a title and content'}
                return render(request,'posts/edit.html' , context)


