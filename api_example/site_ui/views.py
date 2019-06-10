from django.shortcuts import render

# Create your views here.


def glav(request):
    return render(request, 'site_ui/index.html')


def sovr_proza(request):
    return render(request, 'site_ui/index2.html')


def biograph(request):
    return render(request, 'site_ui/index3.html')


def comics(request):
    return render(request, 'site_ui/index4.html')

