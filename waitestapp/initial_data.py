# -*- coding: utf-8 -*-
"""
Created on Fri Nov  7 19:10:08 2014

@author: Reed
"""
#
#CHECKING MECHANISM FOR NUMBERS, MAKE SURE THEY ARE SENSIBLE

capacity_json = [{"Provider_Name":"Doctor 1","Hours_Per_Day":"8","Days_Per_Year":"48","Position":"Physician","Team":"Team A"},
                 {"Provider_Name":"Doctor 2","Hours_Per_Day":"8","Days_Per_Year":"48","Position":"Physician","Team":"Team A"},
                 {"Provider_Name":"Doctor 3","Hours_Per_Day":"8","Days_Per_Year":"50","Position":"Physician","Team":"Team B"},
                 {"Provider_Name":"Nurse 1","Hours_Per_Day":"8","Days_Per_Year":"50","Position":"Nurse Practitioner","Team":"Team B"},
                 {"Provider_Name":"Assist. 1","Hours_Per_Day":"8","Days_Per_Year":"50","Position":"Physician Assistant","Team":"Team A"}]                 
                 
aff_json = [{"Provider":"Doctor 1","Patient":"Patient A"},
            {"Provider":"Doctor 1","Patient":"Patient B"},
            {"Provider":"Doctor 2","Patient":"Patient C"},
            {"Provider":"Doctor 2","Patient":"Patient D"},
            {"Provider":"Doctor 3","Patient":"Patient E"},
            {"Provider":"Doctor 3","Patient":"Patient F"}]
            
attr_json = [{"Physician":"Doctor 1", "Males":"900", "Females":"900", "Panel_Size":"1800"},
             {"Physician":"Doctor 2", "Males":"900", "Females":"900", "Panel_Size":"1800"},
             {"Physician":"Doctor 3", "Males":"900", "Females":"900", "Panel_Size":"1800"}]


cont_json = [{"Rule":"Gender:M AND Age_Range:0-24 AND Visit_Type:Acute"},{"Continuity":"Do Not Share"}]                 

del_json = [{"Rule":"Gender:F AND Age_Range:0-24 AND Visit_Type:Acute"}, {"Delegation":"Nurse 1"}]

pat_json = [{"Patient_Name":"Patient A","Patient_Gender":"M","Age":"24","Chronic_Conditions":"0"},
            {"Patient_Name":"Patient B","Patient_Gender":"F","Age":"58","Chronic_Conditions":"2"},
            {"Patient_Name":"Patient C","Patient_Gender":"F","Age":"12","Chronic_Conditions":"1"},
            {"Patient_Name":"Patient D","Patient_Gender":"M","Age":"74","Chronic_Conditions":"4"}, 
            {"Patient_Name":"Patient E","Patient_Gender":"F","Age":"35","Chronic_Conditions":"2"},
            {"Patient_Name":"Patient F","Patient_Gender":"M","Age":"31","Chronic_Conditions":"1"}]