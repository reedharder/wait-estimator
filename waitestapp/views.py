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

def waitapp_utilization(request):#get doctors in list
    provTable = request.session['capacity_table']
   
    import numpy as np
    from itertools import product       
    
    #parse doctors and their hours
    prov_to_num={}
    num_to_prov={}
    phys_to_num={}
    num_to_phys={}
    phys_mins={}
    non_phys_mins={}
    for j, row in enumerate(provTable):
        i = j + 1 #reserve doctor code 0 for any doctor        
         #map names to numbers
        print(row)
        prov_to_num[row['Provider Name']] = i        
        num_to_prov[i] = row['Provider Name']
        #note pprovider avg. min per day
        if row['Position'] == 'Physician': 
            phys_to_num[row['Provider Name']] = i        
            num_to_phys[i] = row['Provider Name']
            phys_mins[i]=60*int(row['Hours Per Day'])*(int(row['Days Per Year']))/360
        else:
            non_phys_mins[i]=60*int(row['Hours Per Day'])*(int(row['Days Per Year']))/360
            
    
    #generate list of shared categories
    #share everything if default 
    if request.session['defCont'] == 'share':
        shared_categories = [categ for categ in product([1,2],[1,2,3,4,5,6], [0,1,2,3],[1,2,3],phys_to_num.values())]
    else:
        shared_categories = []
    for line in request.session['cont_table']:
        rule_dict={}
        rule_categories=[[],[],[],[]]
        #dictionary for each rule component
        for ind, element in enumerate(line['Rule'].split(' ')):
            ##print('el: %s' % element)
            if ind % 2 == 0: # if not a boolean element
                rule_dict[element.split(':')[0]]=element.split(':')[1]
        if 'Gender' in rule_dict:
            rule_categories[0] = [2] if rule_dict['Gender']=='M' else [1] 
        else:
            rule_categories[0] = [1,2]
        if 'Age' in rule_dict:
            rule_categories[1]=list(range(age_bracket(rule_dict['Age'].split('-')[0]), age_bracket(rule_dict['Age'].split('-')[1]) + 1))
        else:
            rule_categories[1]=[1,2,3,4,5,6]
        if 'Chronic' in rule_dict:
            rule_categories[2]=list(range(chron_bracket(rule_dict['Cond'].split('-')[0]), chron_bracket(rule_dict['Age'].split('-')[1]) + 1))
        else:
            rule_categories[2]=[0,1,2,3]
        if 'Visit' in rule_dict:
            rule_categories[3]=[visit_bracket(rule_dict['Visit'])]
        else:
            rule_categories[3]=[1,2,3]
        if 'Provider' in rule_dict:
            rule_categories[4]=[phys_to_num[rule_dict['Provider']]]
        else:
            rule_categories[4]=phys_to_num.values()
        # list of category integer indices for which the current rule applies
        rule = line['Continuity']        
        
        categories_affected=[categ for categ in product(rule_categories[0], rule_categories[1], rule_categories[2], rule_categories[3], rule_categories[4])]
        
        for category in categories_affected:
            if rule == 'Share':
                shared_categories.append(category)
            #if default share and rule is no share, remove categry from shared list
            elif request.session['defCont'] == 'share' and rule == "Do Not Share" and (category in  shared_categories):
                while category in shared_categories: shared_categories.remove(category)  
                    
                  
    #estimate panel composition of each based on namcs
    request.session['prov_to_num'] = prov_to_num
    request.session['phys_to_num'] = phys_to_num
    panelTable = request.session['attr_table']
    #generate panels:
    from collections import Counter
    #lookup index for each visit type   
    category_full_to_ind = {}
    nums = []
    freqs = []
    durs = []
    doc_lookup = []
    ind = 0 # start increment counter
    phys_demand = {} #dictionary of demand per physician
    for panel in panelTable:
        acute_demand = 0 # start counter of demand
        prev_demand = 0
        chronic_demand = 0
        doc = prov_to_num[panelTable['Physician']]
        num_males = int(panelTable['Males'])
        num_females = int(panelTable['Females'])
        #generate panel accordin to male female ratio and namcs proportions
        male_dist = Counter(np.random.choice(initial_data.female_cats, num_females, initial_data.female_p))
        female_dist = Counter(np.random.choice(initial_data.female_cats, num_females, initial_data.female_p))
        #get full distribution of patient types on panel
        panel_dict = male_dist + female_dist
        #generate import simulation data
        for patient_category in panel_dict:
            #ACUTE            
            #input sex,age,chron,visit, doc           
            category_full_to_ind[(int(patient_category[0]),int(patient_category[1]),int(patient_category[0]),1,int(doc))] = ind
            nums.append(int(panel_dict[patient_category])) #append number represented
            #input sex, age, chron, visit
            freq =initial_data.freq_dict(int(patient_category[0]),int(patient_category[1]),int(patient_category[2]),1)
            dur =initial_data.durs_dict(int(patient_category[0]),int(patient_category[1]),int(patient_category[2]),1)
            freqs.append(freq)
            durs.append(dur)      
            #add to acute demand
            acute_demand += int(panel_dict[patient_category])*freq*360*dur*(1/60)
            doc_lookup.append(int(doc))            
            ind += 1 #increment index
            #PREV
            #input sex,age,chron,visit, doc
            category_full_to_ind[(int(patient_category[0]),int(patient_category[1]),int(patient_category[0]),2,int(doc))] = ind
            nums.append(panel_dict[patient_category]) #append number represented
            #input sex, age, chron, visit
            freq = initial_data.freq_dict(int(patient_category[0]),int(patient_category[1]),int(patient_category[2]),2)
            dur = initial_data.durs_dict(int(patient_category[0]),int(patient_category[1]),int(patient_category[2]),2)
            freqs.append(freq)
            durs.append(dur) 
            #add to prev demand
            prev_demand += int(panel_dict[patient_category])*freq*360*dur*(1/60)
            doc_lookup.append(int(doc))
            ind +=1 #increment index
            #CHRONIC
            #input sex,age,chron,visit, doc
            category_full_to_ind[(int(patient_category[0]),int(patient_category[1]),int(patient_category[0]),3,int(doc))] = ind
            nums.append(panel_dict[patient_category]) #append number represented
            #input sex, age, chron, visit
            freq =initial_data.freq_dict(int(patient_category[0]),int(patient_category[1]),int(patient_category[2]),3)
            dur =initial_data.durs_dict(int(patient_category[0]),int(patient_category[1]),int(patient_category[2]),3)
            freqs.append(freq)
            durs.append(dur)   
            #add to acute demand
            chronic_demand += int(panel_dict[patient_category])*freq*360*dur*(1/60)
            doc_lookup.append(int(doc))
            ind +=1 #increment index
        #add doctor demand to dictionary, list is demands by visit, total demand, placeholders for total capacity, team name,  team members, and capacity-demand, and finally panel size
        phys_demand[panelTable['Physician']] = [acute_demand, prev_demand, chronic_demand, sum((acute_demand, prev_demand, chronic_demand)), None, None, None, None , num_males + num_females]
    
    #convert list of shared categories to indices
    shared_categories = [category_full_to_ind(category) for category in shared_categories]
    #save nums, freqs, durs,  category_full_to_ind, shared_categories, phys_mins
    request.session['nums'] = nums
    request.session['freqs'] = freqs
    request.session['durs'] = durs
    request.session['shared_categories'] = shared_categories
    request.session['phys_mins'] = phys_mins
    request.session['doc_lookup'] = doc_lookup
    #prepare capacity
    capacity_table = request.session['capacity_table']
    ##phys_capacity = {}
    team_capacity = {}  
    ##phys_teams = {}
    #create lookup dictionary to map patient conditions to index 
    '''
    category_product=itertools.product([1,2],[0,1,2,3,4,5],[0,1,2,3],phys_to_num.values())
    category_name_key_mapping={}
    for ind, category in enumerate(category_product):
        category_name_key_mapping[category]=ind
        ind_to_category[ind] = category 
        
    #dictionary keyed to integer representations for each key (gender, age bracket, chron condition bracket, physician)
    request.session['category_name_key_mapping'] = category_name_key_mapping
    request.session['ind_to_category'] = ind_to_category   
    '''        
    #note capacities for teams and physicians (and compile a list of physicians for each team)
    for record in capacity_table:
        if record['Position'] == 'Physician':
            phys_demand[record['Provider Name']][4] = int(record['Hours Per Day'])*int(record['Days Per Year'])
            phys_demand[record['Provider Name']][5] = record['Team'] #team name
            #imbalance
            phys_demand[record['Provider Name']][7] = phys_demand[record['Provider Name']][4] - phys_demand[record['Provider Name']][3]
        try:
            team_capacity[record['Team']][0] += [record['Position'] + record['Provider Name']]
            team_capacity[record['Team']][1] += int(record['Hours Per Day'])*int(record['Days Per Year'])
        except KeyError:
            team_capacity[record['Team']] = ['','']
            team_capacity[record['Team']][0] = [record['Position'] + record['Provider Name']]
            team_capacity[record['Team']][1] = int(record['Hours Per Day'])*int(record['Days Per Year'])
    for phys in phys_demand: # get list of team members for each physician
        phys_demand[phys][6]=team_capacity[phys_demand[phys][5]][0]
    return render(request, 'waitestapp/waitapp_utilization.html', {'phys_demand':phys_demand})
    
def waitapp_results(request):    
    if request.method == 'POST':
        
        
        gender  = request.POST['gender']
        gender = gender_bracket(gender)
        age  = request.POST['gender']
        age=int(age)        
        chron = request.POST['chron']
        chron=int(chron[0])
        doc = request.POST['doc']
        prov_to_num = request.session['prov_to_num'] 
        doc = prov_to_num[doc]
        visit = request.POST['visit']
        visit = visit_bracket(visit)
        if request.POST['type'] == 'rowSelect':
            pass
        
    else:
        from  waitestapp import waitsimulator
        nums=request.session['nums'] 
        freqs=request.session['freqs'] 
        durs=request.session['durs'] 
        shared_categories = request.session['shared_categories'] 
        phys_mins=request.session['phys_mins'] 
        doc_lookup= request.session['doc_lookup']
        K=waitsimulator.mat_sim(cut_off=0, carve_out=False,  days=1000, freqs=freqs, durs=durs,  nums=nums, num_classes=(len(durs)/3), nurse_dict={}, phys_mins=phys_mins, doc_lookup=doc_lookup, shared_categories=shared_categories)
            
    return render(request, 'waitestapp/waitapp_results.html', {'phys_list':request.session['phys_list']})

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
            team_capacity[record['Team']][0] += [record['Position'] + record['Provider Name']] #team list
            team_capacity[record['Team']][1] += int(record['Hours Per Day'])*int(record['Weeks Per Year'])
        except KeyError:
            team_capacity[record['Team']][0] = [record['Position'] + record['Provider Name']] #team list
            team_capacity[record['Team']][1] += int(record['Hours Per Day'])*int(record['Weeks Per Year'])
    
    return render(request, 'waitestapp/scenario_utilization.html', {'phys_capacity':phys_capacity,'team_capacity':team_capacity, })
 
def scenario_results(request):
    return render(request, 'waitestapp/scenario_results.html')


# METHODS FOR VIEWS
#replaces spaces in dictionary keys with underscores for ease of use in templates
def key_clean(table):
    new_table = []
    for old_dict in table:
        new_dict = {}
        for key in old_dict:
            new_dict[key.replace(" ","_")] = old_dict[key]
        new_table.append(new_dict)
    return new_table

def coding_for_provider(provider_type):
    if provider_type == "Physician":
        coding = 1
    else: 
        coding = 2
    return coding
    
    
#sorts age into an age bin    
def visit_bracket(visit):
            
    if visit == 'Acute':
        visit_bracket = 1
    elif visit == 'Preventative':
        visit_bracket = 2
    else:
        visit_bracket = 3
    return visit_bracket

def gender_bracket(gender):
            
    if gender == 'M':
        gender_bracket = 2   
    else:
        gender_bracket = 1
    return gender_bracket
    

#sorts age into an age bin    
def age_bracket(age):
    age= int(age)        
    if age <15:
        age_bracket = 0
    elif age >= 15 and age <=24:
        age_bracket = 1
    elif age >= 25 and age <=44:
        age_bracket =2
    elif age >= 45 and age <=64:
        age_bracket =3
    elif age >= 65 and age <=74:
        age_bracket =4
    else:
        age_bracket = 5
    return age_bracket
    
   
    
#sorts number of chronic conditions into bin
def chron_bracket(chron):
    chron=int(chron)
    if chron == 0:
        chron_bracket = 0
    elif chron == 1:
        chron_bracket = 1
    elif chron == 2:
        chron_bracket = 2
    elif chron >= 3:
        chron_bracket = 3
    return chron_bracket
        