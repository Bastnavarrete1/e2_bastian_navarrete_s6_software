from django.http import HttpResponse

def home(request):
    return HttpResponse("CloudWorld funcionando")