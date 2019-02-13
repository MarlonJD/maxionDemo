from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from .models import DataSet
from .forms import DocumentForm
from .functions import *

from django.views.decorators.csrf import csrf_protect

def index(request):
    return render(request, 'data/index.html', 
    {'data': DataSet.objects.all(), 'default': DataSet.objects.filter(default=True)})

@csrf_protect
def createData(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = DocumentForm()
    return render(request, 'data/createData.html', {
        'form': form
    })

def dataView(request, uuid):
    return render(request, 'data/dataView.html', 
    {'data':DataSet.objects.get(uuid=uuid)})

def getJSON(request):
    try:
        d = DataSet.objects.values().get(default=True)
    except (KeyError, DataSet.DoesNotExist):
        return JsonResponse({'failed': 'There is no content here'})
    else:
        d["content"] = "https://maxion.ff-api.com/media/" + d["content"]
        return JsonResponse(d)

def delete(request, uuid):
    try:
        DataSet.objects.get(uuid=uuid).delete()
    except (KeyError, DataSet.DoesNotExist):
        return HttpResponseRedirect('/?error_code=0001')
        #{'error_mesage': "Herşey silinirken bir hata oluştu."})
    finally:
        return HttpResponseRedirect('/')

def deleteAll(request):
    try:
        DataSet.objects.all().delete()
    except (KeyError, DataSet.DoesNotExist):
        return HttpResponseRedirect('/?error_code=0002') 
        #{'error_mesage': "Herşey silinirken bir hata oluştu."})
    finally:
        return HttpResponseRedirect('/')

def makeDefault(request, uuid):
    try:
        d = DataSet.objects.get(default=True)
        d.default = False
        d.save()
    except (KeyError, DataSet.DoesNotExist):
        return HttpResponseRedirect('/')
        #{'error_mesage': "Varsayılan olurken bir sorun oluştu."})
    finally:
        e = DataSet.objects.get(uuid=uuid)
        e.default = True
        e.save()
        return HttpResponseRedirect('/?changed=True')
