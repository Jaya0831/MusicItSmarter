from django.shortcuts import render
from django.views.decorators import csrf
from MusicItSmarter.models import Musicinfo

# Create your views here.

def playMusic(request):
    ctx={}
    u = request.POST.get("emoji", '')
    if u=="happy":
        ctx['rlt']=Musicinfo.objects.filter(happy=True)
    elif u=="sad":
        ctx['rlt'] = Musicinfo.objects.filter(sad=True)
    elif u=="driving":
        ctx['rlt'] = Musicinfo.objects.filter(driving=True)

    return render(request, 'musicPlaying.html', ctx)
