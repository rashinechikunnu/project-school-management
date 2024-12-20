from django.shortcuts import render, redirect
from django.http import Http404
from .models import school
from .forms import schoolForm

# Create your views here.

# home
def home(request):
    return render(request,'home.html')

# create form
def addStudy(request):
    if request.POST:
        frm = schoolForm(request.POST)
        if frm.is_valid():
            frm.save()
           
            return redirect('list')  
    else:
        frm = schoolForm()

    return render(request, 'add_study.html', {'frm': frm})

# view list
def view(request):
    try:
        orm = school.objects.all()
    except Exception as e:
        orm = []
        print(f"Error fetching data: {e}")
    
    return render(request, 'list.html', {'orm': orm})

# edit list
def edit(request, pk):
    try:
        edt = school.objects.get(pk=pk)
    except school.DoesNotExist:
        raise Http404("School not found")

    if request.POST:
        frm = schoolForm(request.POST, request.FILES, instance=edt)
        if frm.is_valid():
            frm.save()
          
            return redirect('list')  
    else:
        frm = schoolForm(instance=edt)

    return render(request, 'edit.html', {'frm': frm})

# delete list
def delete(request, pk):
    try:
        delf = school.objects.get(pk=pk)
    except school.DoesNotExist:
        raise Http404("School not found")

    try:
        delf.delete()
    except Exception as e:
        print(f"Error deleting: {e}")

    orm = school.objects.all()
    return render(request, 'list.html', {'orm': orm})
