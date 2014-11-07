from django.shortcuts import render, render_to_response
from django.contrib.formtools.wizard.views import SessionWizardView
import waitestapp
CURRENT_TEMPLATES={'capacity':'waitestapp/waitapp_capacity.html', 
                   'aff':'waitestapp/waitapp_aff.html',
                   'attr':'waitestapp/waitapp_attr.html',
                   'cont':'waitestapp/waitapp_contrule.html',
                   'del':'waitestapp/waitapp_delrule.html'}

CURRENT_FORMS = [("capacity", waitestapp.forms.CurrCapacityForm),
                 ("aff", waitestapp.forms.CurrAffForm),
                 ("attr", waitestapp.forms.CurrAttForm),
                 ("cont", waitestapp.forms.CurrContForm),
                 ("del", waitestapp.forms.CurrDelForm)]

class CurrentWizard(SessionWizardView):
    def done(self, form_list, form_dict, **kwargs):
        return render_to_response('waitestapp/waitapp_results.html', {
            'form_data': [form.cleaned_data for form in form_list],
        })

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

def scenario_capacity(request):
    return render(request, 'waitestapp/scenario_capacity.html')
    
def scenario_aff(request):
    return render(request, 'waitestapp/scenario_aff.html')

def scenario_attr(request):
    return render(request, 'waitestapp/scenario_attr.html')
    
def scenario_contrule(request):
    return render(request, 'waitestapp/scenario_contrule.html')

def scenario_delrule(request):
    return render(request, 'waitestapp/scenario_delrule.html')

def scenario_utilization(request):
    return render(request, 'waitestapp/scenario_utilization.html')


def scenario_results(request):
    return render(request, 'waitestapp/scenario_results.html')
