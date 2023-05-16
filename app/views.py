from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import FormView
from app.models import *
from app.forms import *

# Create your views here.

class cbv_form(FormView):
    template_name='cbv_form.html'
    form_class=SchoolForm

    def form_valid(self, form):
        form.save()
        return HttpResponse('Data Inserted Successfully')
