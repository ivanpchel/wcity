from django.shortcuts import render

# Create your views here.
#from django.http import HttpResponse
#from django.template import loader

from .models import Fenster
from random import randint


def index(request):
   
   # test_creation(1)
   # test_creation(2)
   # test_creation(3)
   # test_creation(4)
   # test_creation(5)
    
    fenster_list = Fenster.objects.order_by("id")
    
    context = {
	"window_list": fenster_list,	
    }

    #return HttpResponse(template.render(context))
    return render(request, 'fenster/index.html', context)

def test_creation(number):

    f = Fenster(
        window_width=randint(100, 256),
        window_height=randint(100, 256),
        window_number=number,
    )
    f.save()
