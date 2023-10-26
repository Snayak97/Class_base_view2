from django.shortcuts import render

# Create your views here.
from django.views.generic import *
from app.models import *
from django.http import HttpResponse
from app.forms import *

class Fbc_temp(View):
    def get(self,request):
        d={'name':'soumya'}
        return render(request,'Fbc_temp.html',d)

#insert Fbv
def insert_fbv(request):
    SFO=StudentForm()
    d={'SFO':SFO}
    if request.method=='POST':
        SFD=StudentForm(request.POST)
        if SFD.is_valid():
            SFD.save()
            return HttpResponse('data is saved')
    return render(request,'insert_fbv.html',d)

#insert CBV
class Cbv_insert(View):
    def get(self,request):
        SFO=StudentForm()
        d={'SFO':SFO}
        return render(request,'Cbv_insert.html',d)
    

    def post(self,request):
        SFD=StudentForm(request.POST)
        if SFD.is_valid():
            SFD.save()
            return HttpResponse('Cbv_insert')
class temp(TemplateView):
    template_name='temp.html'
