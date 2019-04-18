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

    try:

        if request.method == 'POST':
            fenster_id = request.POST['selected_fenster']
            buy(fenster_id)
        
        fenster_list = Fenster.objects.filter(is_buy=False).order_by("id")
        buyed_count = Fenster.objects.filter(is_buy=True).count()
        in_stock_count = len(fenster_list)   	
        context = {
            "window_list": fenster_list,
            "buyed_count": buyed_count,
            "in_stock_count": in_stock_count,	
         }

        return render(request, 'fenster/index.html', context)
    except:
        i = 1
	
def buy(fenster_id):
    Fenster.objects.filter(id=fenster_id).update(is_buy=True)
    #правильней получать через get
    #Fenster.objects.filter(id=fenster_id).delete()

def test_creation(number):

    f = Fenster(
        window_width=randint(100, 256),
        window_height=randint(100, 256),
        window_number=number,
    )
    f.save()
