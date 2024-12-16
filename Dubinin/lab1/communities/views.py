from django.shortcuts import render, redirect
from .models import Comm
from django.contrib.auth.decorators import login_required
from . import forms 

def communities_list(request):
    communities = Comm.objects.all().order_by('-date')
    return render(request, 'communities/communities_list.html', {'communities': communities})

def communitie_page(request, slug):
    community = Comm.objects.get(slug=slug)
    return render(request, 'communities/communitie_page.html', {'community': community})

@login_required(login_url="/users/login/")
def communitie_new(request):
    if request.method == 'POST': 
        form = forms.CreateComm(request.POST, request.FILES) 
        if form.is_valid():
            newcommunities = form.save(commit=False) 
            newcommunities.author = request.user 
            newcommunities.save()
            return redirect('posts:list')
    else:
        form = forms.CreateComm()
    return render(request, 'communities/communitie_new.html', { 'form': form})