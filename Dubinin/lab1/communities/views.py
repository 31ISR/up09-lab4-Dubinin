from django.shortcuts import render
from .models import Comm

def communities_list(request):
    communities = Comm.objects.all().order_by('-date')
    return render(request, 'communities/communities_list.html', {'communities': communities})

def communitie_page(request, slug):
    community = Comm.objects.get(slug=slug)
    return render(request, 'communities/communitie_page.html', {'community': community})