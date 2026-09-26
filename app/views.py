from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario, Tarefa


def home(request):
    return render(request, 'home.html')

def usuario_form(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')
        usuario = Usuario(nome=nome, email=email, cpf=cpf)
        usuario.save()
        return redirect('app:usuario_list')
    return render(request, 'usuario_form.html')

def usuario_list(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuario_list.html', {'usuarios': usuarios})

def usuario_edit(request, pk):
    usuario = get_object_or_404(Usuario, id=pk)

    if request.method=='POST':
        usuario.nome = request.POST.get('nome')
        usuario.cpf = request.POST.get('cpf')
        usuario.email = request.POST.get('email')

        usuario.save()
        return redirect ("app:usuario_list")
    return render (request, 'usuario_form.html', {'usuario':usuario})




def usuario_delete(request, pk):
        usuario = get_object_or_404(Usuario, id=pk) 
        usuario.delete()
        return redirect('app:usuario_list')



def tarefa_form(request):
    usuarios = Usuario.objects.all()

    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        status = 'Concluída' if request.POST.get('status') == 'Concluída' else 'Pendente'
        data_limite = request.POST.get('data_limite')
        responsavel_id = request.POST.get('responsavel')

        Tarefa.objects.create(
            titulo=titulo,
            descricao=descricao,
            status=status,
            data_limite=data_limite,
            responsavel_id=responsavel_id,
        )
        return redirect('app:tarefa_list')

    return render(request, 'tarefa_form.html', {'usuarios': usuarios})


def tarefa_list(request):
    tarefas = Tarefa.objects.all()
    return render(request, 'tarefa_list.html', {'tarefas':tarefas})


def tarefa_edit(request,pk):
    tarefa = get_object_or_404(Tarefa, id=pk)
    usuarios = Usuario.objects.all()

    if request.method=='POST':
        tarefa.titulo = request.POST.get('titulo')
        tarefa.descricao = request.POST.get('descricao')
        tarefa.status = request.POST.get('status')
        tarefa.data_limite = request.POST.get('data_limite')
        tarefa.responsavel_id = request.POST.get('responsavel')

        tarefa.save()
        return redirect("app:tarefa_list")
    return  render (request, 'tarefa_form.html', {'tarefa':tarefa, 'usuarios':usuarios})

def tarefa_delete(request, pk):
    tarefa = get_object_or_404(Tarefa, id=pk)
    tarefa.delete()
    return redirect('app:tarefa_list')