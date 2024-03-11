from django.shortcuts import render, redirect

from my_app.forms import project_form


# Create your views here.
def todo(request):
    return render(request,'index.html')
def dash(request):
    return render(request,'dashboard.html')
def dashadmin(request):
    return render(request,'adminindex.html')
def formhtml(request):
    data=project_form()
    if request.method=='POST':
        obj=project_form(request.POST)
        if obj.is_valid():
            obj.save()
            return redirect("/")
    # print(data)
    return render(request,'modelform.html',{'formkey':data})



