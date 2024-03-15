from django.shortcuts import render

# Create your views here.
def forloop(request):
    d={'Name':'Arya'}
    return render(request, 'forloop.html',d)
