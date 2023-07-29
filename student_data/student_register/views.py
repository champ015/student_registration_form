from django.shortcuts import render,redirect
from .forms import studentform
from .models import employee
#from .import views 
def studform(request,id=0):
    if request.method=='GET':
        if id==0:
             form=studentform()
        else:
             student=employee.objects.get(pk=id)
             form=studentform(instance=student)
        return render(request,'stud_register/stud_form.html',{'form':form})
    else:
         student=employee.objects.get(pk=id)
         form=studentform(request.POST,instance=student)
         if form.is_valid():
            form.save()
    return redirect('/Radha/Kanha')
def studlist(request):
    context={'student_list':employee.objects.all()}
    return render(request,'stud_register/stud_list.html',context)
def deletedata(request,id):
    emp=employee.objects.get(pk=id)
    emp.delete()
    return redirect('/Radha/Kanha')
# Create your views here.
