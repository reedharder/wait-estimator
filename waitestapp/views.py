from django.shortcuts import render

def home_view(request):
    return render(request, 'waitestapp/base_site.html')

def waitapp_capacity(request):
    return render(request, 'waitestapp/waitapp_capacity.html')
    
def waitapp_aff(request):
    return render(request, 'waitestapp/waitapp_aff.html')

def waitapp_attr(request):
    return render(request, 'waitestapp/waitapp_attr.html')
    
def waitapp_contrule(request):
    return render(request, 'waitestapp/waitapp_contrule.html')

def waitapp_delrule(request):
    return render(request, 'waitestapp/waitapp_delrule.html')

def waitapp_utilization(request):
    return render(request, 'waitestapp/waitapp_utilization.html')


def waitapp_results(request):
    return render(request, 'waitestapp/waitapp_results.html')
