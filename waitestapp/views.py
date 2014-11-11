from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.contrib.formtools.wizard.views import SessionWizardView
from  waitestapp import initial_data


'''

CURRENT_TEMPLATES={'capacity':'waitestapp/waitapp_capacity.html', 
                   'aff':'waitestapp/waitapp_aff.html',
                   'attr':'waitestapp/waitapp_attr.html',
                   'cont':'waitestapp/waitapp_contrule.html',
                   'del':'waitestapp/waitapp_delrule.html',
                   'ut':'waitestapp/waitapp_utilization.html',
                   'res':'waitestapp/waitapp_utilization.html',
                   's_capacity':'waitestapp/scenario_capacity.html', 
                   's_aff':'waitestapp/scenario_aff.html',
                   's_attr':'waitestapp/scenario_attr.html',
                   's_cont':'waitestapp/scenario_contrule.html',
                   's_del':'waitestapp/scenario_delrule.html',
                   's_ut':'waitestapp/scenario_utilization.html',
                   's_res':'waitestapp/scenario_utilization.html',             
                   
                   }
                   ## ADD SCENARIO TABS!

CURRENT_FORMS = [("capacity", waitestapp.forms.CurrCapacityForm),
                 ("aff", waitestapp.forms.CurrAffForm),
                 ("attr", waitestapp.forms.CurrAttForm),
                 ("cont", waitestapp.forms.CurrContForm),
                 ("del", waitestapp.forms.CurrDelForm),
                 ("ut", waitestapp.forms.CurrDelForm),
                 ("res", waitestapp.forms.CurrDelForm),
                 ("capacity", waitestapp.forms.CurrCapacityForm),
                 ("aff", waitestapp.forms.CurrAffForm),
                 ("attr", waitestapp.forms.CurrAttForm),
                 ("cont", waitestapp.forms.CurrContForm),
                 ("del", waitestapp.forms.CurrDelForm),


]
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
    if request.method == 'POST':
        import ast
        table = ast.literal_eval(request.POST['id_table'])
        print(table)
        #get lists of physicians, non physicians
        phys_list=[record['Provider Name'] for record in table if record['Position']=='Physician']
        nonphys_list=[record['Provider Name'] for record in table if record['Position']!='Physician']
        request.session['phys_list'] = phys_list
        request.session['nonphys_list'] = nonphys_list
        request.session['capacity_table'] = table
        
        return HttpResponse('ok')
    try: 
        table_data = request.session['capacity_table']         
    except KeyError:
        table_data = initial_data.capacity_json 
    else:
        table_data = key_clean(table_data)
        
    return render(request, 'waitestapp/waitapp_capacity.html', {'table_data':table_data})
    
def waitapp_aff(request):
    if request.method == 'POST':
        import ast
        table = ast.literal_eval(request.POST['id_table'])
        request.session['aff_table'] = table
    try: 
        table_data = request.session['aff_table']
    except KeyError:
        table_data = initial_data.aff_json 
    else:
        table_data = key_clean(table_data)
    return render(request, 'waitestapp/waitapp_aff.html',{'phys_list':request.session['phys_list'], 'table_data':table_data})

def waitapp_attr(request):
    if request.method == 'POST':
        import ast
        table = ast.literal_eval(request.POST['id_table'])
        patTable = ast.literal_eval(request.POST['patTable'])
        request.session['attr_table'] = table
        request.session['patTable'] = patTable
    try: 
        table_data = request.session['attr_table']
        pat_table_data = request.session['patTable']
    except KeyError:
        table_data = initial_data.attr_json 
        pat_table_data = initial_data.pat_json 
    else:
        table_data = key_clean(table_data)
        pat_table_data = key_clean(pat_table_data)
    return render(request, 'waitestapp/waitapp_attr.html', {'phys_list':request.session['phys_list'],'table_data':table_data, 'pat_table_data':pat_table_data})
    
def waitapp_contrule(request):
    if request.method == 'POST':
        import ast
        table = ast.literal_eval(request.POST['id_table'])
        request.session['cont_table'] = table
        request.session['defCont'] = request.POST['defCont']
    try: 
        table_data = request.session['cont_table']
        defCont = request.session['defCont']
        if defCont == "share":
            Share = "selected"
            NoShare = ""
        else:
            Share = ""
            NoShare = "selected"            
    except KeyError:
        table_data = initial_data.cont_json 
        Share = "selected"
        NoShare = ""       
    else:
        table_data = key_clean(table_data)
    return render(request, 'waitestapp/waitapp_contrule.html', {'phys_list':request.session['phys_list'],'table_data':table_data, 'share':Share, 'noshare':NoShare} )

def waitapp_delrule(request):
    if request.method == 'POST':
        import ast
        table = ast.literal_eval(request.POST['id_table'])
        request.session['del_table'] = table
    try: 
        table_data = request.session['del_table']
    except KeyError:
        table_data = initial_data.del_json 
    else:
        table_data = key_clean(table_data)
    return render(request, 'waitestapp/waitapp_delrule.html', {'nonphys_list':request.session['nonphys_list'],'table_data':table_data})

def waitapp_utilization(request):
    capacity_table = request.session['capacity_table']
    phys_capacity = {}
    team_capacity = {}        
    #note capacities for teams and physicians (and compile a list of physicians for each team)
    for record in capacity_table:
        if record['Position'] == 'Physician':
            phys_capacity[record['Provider Name']] = int(record['Hours Per Day'])*int(record['Weeks Per Year'])
        try:
            team_capacity[record['Team']][0] += [record['Position'] + record['Provider Name']]
            team_capacity[record['Team']][1] += int(record['Hours Per Day'])*int(record['Weeks Per Year'])
        except KeyError:
            team_capacity[record['Team']][0] = [record['Position'] + record['Provider Name']]
            team_capacity[record['Team']][1] += int(record['Hours Per Day'])*int(record['Weeks Per Year'])
    return render(request, 'waitestapp/waitapp_utilization.html', {'phys_capacity':phys_capacity,'team_capacity':team_capacity })

def waitapp_results(request):    
    return render(request, 'waitestapp/waitapp_results.html')

def scenario_capacity(request):
    if request.method == 'POST':
        import ast
        table = ast.literal_eval(request.POST['id_table'])
        #get lists of physicians, non physicians
        phys_list=[record['Provider Name'] for record in table if record['Position']=='Physician']
        nonphys_list=[record['Provider Name'] for record in table if record['Position']!='Physician']
        request.session['s_phys_list'] = phys_list
        request.session['s_nonphys_list'] = nonphys_list
        request.session['s_capacity_table'] = table
    try: 
        table_data = request.session['s_capacity_table']
    except KeyError:
        table_data = request.session['capacity_table'] 
    else:
        table_data = key_clean(table_data)
    return render(request, 'waitestapp/scenario_capacity.html', {'table_data':table_data})
    
    
def scenario_aff(request):
    if request.method == 'POST':
        import ast
        table = ast.literal_eval(request.POST['id_table'])
        request.session['s_aff_table'] = table
    try: 
        table_data = request.session['s_aff_table']
    except KeyError:
        table_data = request.session['aff_table'] 
    else:
        table_data = key_clean(table_data)
    return render(request, 'waitestapp/scenario_aff.html',{'phys_list':request.session['s_phys_list'], 'table_data':table_data})

def scenario_attr(request):
    if request.method == 'POST':
        import ast
        table = ast.literal_eval(request.POST['id_table'])
        request.session['s_attr_table'] = table
    try: 
        table_data = request.session['s_attr_table']
    except KeyError:
        table_data = request.session['attr_table'] 
    else:
        table_data = key_clean(table_data)
    return render(request, 'waitestapp/scenario_attr.html', {'phys_list':request.session['s_phys_list'],'table_data':table_data})
    
    
def scenario_contrule(request):
    if request.method == 'POST':
        import ast
        table = ast.literal_eval(request.POST['id_table'])
        request.session['s_cont_table'] = table
        request.session['s_defCont'] = request.POST['defCont']
    try: 
        table_data = request.session['s_cont_table']
        defCont = request.session['s_defCont']
        if defCont == "share":
            Share = "selected"
            NoShare = ""
        else:
            Share = ""
            NoShare = "selected"
    except KeyError:
        table_data = request.session['cont_table']
        defCont = request.session['defCont']
        if defCont == "share":
            Share = "selected"
            NoShare = ""
        else:
            Share = ""
            NoShare = "selected"
    else:
        table_data = key_clean[table_data]
    return render(request, 'waitestapp/scenario_contrule.html', {'phys_list':request.session['s_phys_list'],'table_data':table_data,'share':Share, 'noshare':NoShare} )

def scenario_delrule(request):
    if request.method == 'POST':
        import ast
        table = ast.literal_eval(request.POST['id_table'])
        request.session['s_del_table'] = table
    try: 
        table_data = request.session['s_del_table']
    except KeyError:
        table_data = request.session['del_table'] 
    else:
        table_data = key_clean(table_data)
    return render(request, 'waitestapp/scenario_delrule.html', {'nonphys_list':request.session['s_nonphys_list'],'table_data':table_data})

    

def scenario_utilization(request):
    capacity_table = request.session['s_capacity_table']
    phys_capacity = {}
    team_capacity = {}        
    #note capacities for teams and physicians (and compile a list of physicians for each team)
    for record in capacity_table:
        if record['Position'] == 'Physician':
            phys_capacity[record['Provider Name']] = int(record['Hours Per Day'])*int(record['Weeks Per Year'])
        try:
            team_capacity[record['Team']][0] += [record['Position'] + record['Provider Name']]
            team_capacity[record['Team']][1] += int(record['Hours Per Day'])*int(record['Weeks Per Year'])
        except KeyError:
            team_capacity[record['Team']][0] = [record['Position'] + record['Provider Name']]
            team_capacity[record['Team']][1] += int(record['Hours Per Day'])*int(record['Weeks Per Year'])
    return render(request, 'waitestapp/scenario_utilization.html', {'phys_capacity':phys_capacity,'team_capacity':team_capacity, })
 
def scenario_results(request):
    return render(request, 'waitestapp/scenario_results.html')

#replaces spaces in dictionary keys with underscores for ease of use in templates
def key_clean(table):
    new_table = []
    for old_dict in table:
        new_dict = {}
        for key in old_dict:
            new_dict[key.replace(" ","_")] = old_dict[key]
        new_table.append(new_dict)
    return new_table
