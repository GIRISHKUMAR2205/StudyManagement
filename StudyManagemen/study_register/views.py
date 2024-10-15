from .forms import Studyform
from .models import Study
from django.shortcuts import render,redirect

# Create your views here.

def studylist(request):
    context= {'study_list':Study.objects.all()}
    return render(request,"study_register/study_list.html",context)
def studyform(request,id=0):
    if request.method=="GET":
        if id==0:
            form=Studyform()
        else:
            sid=Study.objects.get(studyid=id)
            form=Studyform(instance=sid)
        sponsors = Study.objects.values_list('sponsorname', flat=True).distinct()
        return render(request,"study_register/study_form.html",{'id':id,'form':form,'sponsors':sponsors})
    else:
        if id==0:
            form=Studyform(request.POST)
        else:
            sid=Study.objects.get(studyid=id)
            form=Studyform(request.POST,instance=sid)
        if form.is_valid():
            form.save()
        return redirect('/')
def studyupdate(request,id):
    if request=="GET":
        sid=Study.objects.get(studyid=id)
        form=Studyform(instance=sid)
        sponsors = Study.objects.values_list('sponsorname', flat=True).distinct()
        return render(request,"study_register/study_form.html",{'form':form,'sponsors':sponsors})
    else:
        sid=Study.objects.get(studyid=id)
        form=Studyform(request.POST,instance=sid)
        if form.is_valid():
            form.save()
        return redirect('/')

def studydelete(request):
    if request.method == "POST":
        # Get the list of selected study ids
        selected_study_ids = request.POST.getlist('selected_studies')
        # Delete the selected studies in bulk
        Study.objects.filter(studyid__in=selected_study_ids).delete()
        # Redirect to the study list page after deletion
        return redirect('study_list')

    return redirect('study_list')

def studyview(request,id):
    sid=Study.objects.get(studyid=id)
    form=Studyform(instance=sid)
    return render(request,"study_register/study_view.html",{'id':id,'form':form})