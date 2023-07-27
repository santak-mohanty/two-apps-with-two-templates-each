from django.shortcuts import render

# Create your views here.
def index1(request):
    return render(request,"index1.html")

def new1(request):
    return render(request,"new1.html")
