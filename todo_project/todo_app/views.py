from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import Task
from . forms import todoform
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView
from django.urls import reverse_lazy



# Create your views here.
class Task_view(ListView):
    model =Task
    template_name='home.html'
    context_object_name='obj1'

class Task_detail(DetailView):
    model =Task
    template_name='detail.html'
    context_object_name='i'
class Task_update(UpdateView):
    model =Task
    template_name='update.html'
    context_object_name='task'
    fields= ('name','priourity','date')
    def get_success_url(self):
        return reverse_lazy('classdetail',kwargs={'pk':self.object.id})
class Task_delete(DeleteView):
    model =Task
    template_name='delete.html'
    success_url=reverse_lazy('class')

def home(request):
    if request.method=='POST':
        name=request.POST.get('name')
        priourity=request.POST.get('priourity')
        date=request.POST.get('date')
        obj=Task(name=name,priourity=priourity,date=date)
        obj.save()
    obj1=Task.objects.all()


    return render(request,'home.html',{'obj1':obj1})

def delete (request,taskid):

    task=Task.objects.get(id=taskid)
    if request.method == 'POST':
        task.delete()
        return redirect ('/')
    return render(request,'delete.html',{'task':task})
def update(request,id):
    task=Task.objects.get(id=id)
    form=todoform(request.POST or None,instance=task )
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'task':task,'form':form})


