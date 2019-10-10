from django.shortcuts import render

from .models import job

def home(request):
    jobs=job.objects #con este simple comando traigo todo lo que necesito de job
    return render(request,'jobs/home.html',{'jobs':jobs}) #se crea la carpeta templates, que reconoce las homepages, y creo la carpeta jobs para no dejar el homepage en la raiz paraevitar confucion
