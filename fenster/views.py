from django.shortcuts import render

# Create your views here.
#from django.http import HttpResponse
#from django.template import loader

import random

def index(request):
   # template = loader.get_template('fenster/index.html')

    a = random.randint(50, 100)
    b = random.randint(50, 100)
    c = random.randint(50, 100)

    colors = ["ffccaa", "aaccff", "cffacs", "12caf1", "25faca", "2312ff"]
    sel1 = random.randint(0, 5)
    sel2 = random.randint(0, 5)
    color1 = colors[sel1]
    color2 = colors[sel2]

    context = {
        "a": a,
        "b": b,
        "c": c,
        "color1": color1,
        "color2": color2
    }
    #return HttpResponse(template.render(context))
    return render(request, 'fenster/index.html', context)

