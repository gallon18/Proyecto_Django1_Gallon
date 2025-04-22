from django.shortcuts import redirect, render

from todo.forms import TareaForm
from .models import Tarea
# Create your views here.
def index(request):
    tareas = Tarea.objects.all()
    context = {'tareas':tareas}
    return render(request, 'todo/index.html',context)

def agregar(request):
    if request.method == "POST":
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TareaForm()
    context = {'form':form}
    return render(request,'todo/agregar.html',context)

def eliminar(request,tarea_id):
    tarea=Tarea.objects.get(id=tarea_id)
    tarea.delete()
    return redirect("index")

def editar(request,tarea_id):
    tarea=Tarea.objects.get(id=tarea_id)
    if request.method == "POST":
        form = TareaForm(request.POST,instance=tarea)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TareaForm(instance=tarea)
    context = {'form':form}
    return render(request,'todo/editar.html',context)
