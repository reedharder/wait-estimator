from django.shortcuts import render

def home_view(request):
    return render(request, 'waitestapp/base_site.html')

def waitapp_capacity(request):
    return render(request, 'waitestapp/waitapp_capacity.html')


