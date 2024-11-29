from django.shortcuts import render

# Create your views here.
def groupp(req):
    return render(req, 'communities_list/groupp.html')