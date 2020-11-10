from django.shortcuts import render
from . import models
from django.http import HttpResponse
# Create your views here.
def index(request):
    data = list(models.quniao.objects.values('time'))
    '''context = {'year': models.Quniaodata.objects.values('year'), 'month': models.Quniaodata.objects.values('month'),
               'day': models.Quniaodata.objects.values('day'), 'hour': models.Quniaodata.objects.values('hour'),
               'min': models.Quniaodata.objects.values('min')}'''
    # context = models.QUNIAODATA.objects.all()
    context = {'data':data}
    print(data)
    return render(request, 'index1.html', context=context)