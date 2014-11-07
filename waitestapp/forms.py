# -*- coding: utf-8 -*-
"""
Created on Thu Nov  6 19:18:39 2014

@author: Reed
"""
from django import forms
from django.forms.widgets import Select, HiddenInput

class CurrCapacityForm(forms.Form):
    table = forms.TextField(widget=HiddenInput())

class CurrAffForm(forms.Form):
    table = forms.TextField(widget=HiddenInput())

class CurrAttForm(forms.Form):
    table = forms.TextField(widget=HiddenInput())
    
class CurrContForm(forms.Form):
    table = forms.TextField(widget=HiddenInput())

class CurrDelForm(forms.Form):
    table = forms.TestField()
    table = forms.TextField(widget=Select(choices=('Share','Do Not Share')))