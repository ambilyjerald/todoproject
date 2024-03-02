from django.shortcuts import render

# Create your views here.
def todo(request):
    return render(request,'index.html')
def dash(request):
    return render(request,'dashboard.html')
def dash1(request):
    return render(request,'index1.html')


