from django.shortcuts import render

# Create your views here.
def todo(request):
    return render(request,'index.html')
def dash(request):
    return render(request,'dashboard.html')
def dashadmin(request):
    return render(request,'adminindex.html')



