from django.shortcuts import render
from .models import Comm

def communities_list(request):
    communities = Comm.objects.all().order_by('-date')
    return render(request, 'communities/communities_list.html', {'communities': communities})