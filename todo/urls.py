from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path
from todo import views
from todo.models import Tarea

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path("agregar/",views.agregar,name="agregar"),
]

def eliminar(request,tarea_id):
    tarea=Tarea.objects.get(id=tarea_id)
    tarea.delete()
    return redirect("index")
