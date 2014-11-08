from django.shortcuts import render, render_to_response
from django.contrib.formtools.wizard.views import SessionWizardView
import waitestapp

'''

CURRENT_TEMPLATES={'capacity':'waitestapp/waitapp_capacity.html', 
                   'aff':'waitestapp/waitapp_aff.html',
                   'attr':'waitestapp/waitapp_attr.html',
                   'cont':'waitestapp/waitapp_contrule.html',
                   'del':'waitestapp/waitapp_delrule.html'}
                   ## ADD SCENARIO TABS!

CURRENT_FORMS = [("capacity", waitestapp.forms.CurrCapacityForm),
                 ("aff", waitestapp.forms.CurrAffForm),
                 ("attr", waitestapp.forms.CurrAttForm),
                 ("cont", waitestapp.forms.CurrContForm),
                 ("del", waitestapp.forms.CurrDelForm)]
                 #ADD SCENARIO FORMS
                 
#Get list of physicians from capacity tab                 
def get_physician_list(wizard):
     # Get cleaned data from capacity step
    cleaned_data = wizard.get_cleaned_data_for_step('capacity')
    if cleaned_data:
        phys_list=[record['Provider Name'] for record in cleaned_data['table'] if record['Position']=='Physician']
    else:
        phys_list = []
    return phys_list
    
#Get list of physicians from capacity tab                 
def get_nonphys_list(wizard):
     # Get cleaned data from capacity step
    cleaned_data = wizard.get_cleaned_data_for_step('capacity')
    if cleaned_data:
        phys_list=[record['Provider Name'] for record in cleaned_data['table'] if record['Position']!='Physician']
    else:
        phys_list = []
    return phys_list
        
class CurrentWizard(SessionWizardView):
    def get_template_names(self):
        return [CURRENT_TEMPLATES[self.steps.current]]    
        
    def get_context_data(self, form, **kwargs):
        context = super(CurrentWizard, self).get_context_data(form=form, **kwargs)
        if self.steps.current == 'aff' or self.steps.current == 'attr':
            phys_list=get_physician_list(self)
            context.update({'phys_list': phys_list})
        return context
    
    def done(self, form_list, form_dict, **kwargs):
        return render_to_response('waitestapp/waitapp_utilization.html', {
            'form_data': [form.cleaned_data for form in form_list],
        })


wizard_view = CurrentWizard.as_view(CURRENT_FORMS)

def current_wizard_view(request):
    return wizard_view(request)
'''


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
