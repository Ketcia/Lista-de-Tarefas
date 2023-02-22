from django.shortcuts import render, redirect
from .models import Tarefa

def home(request):
    tarefa = Tarefa.objects.all()
    return render(request, 'index.html', {'tarefas':tarefa})

def criarTarefa(request):
    return render(request, 'form.html')

def salvar(request):
    titulo = request.POST.get('titulo')
    descricao = request.POST.get('descricao')
    Tarefa.objects.create(titulo=titulo, descricao=descricao)
    return redirect(home)

def editar(request, id):
    tarefa = Tarefa.objects.get(id=id)
    return render(request, 'editar.html', {'tarefas':tarefa})

def update(request, id):
    titulo = request.POST.get('titulo')
    descricao = request.POST.get('descricao')
    tarefa = Tarefa.objects.get(id=id)
    tarefa.titulo = titulo
    tarefa.descricao = descricao
    tarefa.save()
    return redirect(home)

def delete(request, id):
    tarefa = Tarefa.objects.get(id=id)
    tarefa.delete()
    return redirect(home)

def verMais(request, id):
    tarefa = Tarefa.objects.get(id=id)
    return render(request, 'detalhes.html',{'tarefas':tarefa})

def atualiza_stt(request, id):
    tarefa = Tarefa.objects.get(id=id)
    tarefa.status = True
    tarefa.save()
    return redirect(home)
    