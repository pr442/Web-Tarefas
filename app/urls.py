from django.urls import path
from .views import home, usuario_form, usuario_list, usuario_edit, usuario_delete
from .views import tarefa_form, tarefa_list, tarefa_edit, tarefa_delete

app_name = "app"

urlpatterns = [
    path('', home, name='home'),
    path('usuario/', usuario_list, name='usuario_list'),
    path('usuario/cadastrar/', usuario_form, name='usuario_form'),
    path('usuario/editar/<int:pk>', usuario_edit, name='usuario_edit'),
    path('usuario/deletar/<int:pk>', usuario_delete, name='usuario_delete'),
    path('tarefa/cadastrar/', tarefa_form, name='tarefa_form'),
    path('tarefa/', tarefa_list, name='tarefa_list'),
    path('tarefa/editar/<int:pk>', tarefa_edit, name='tarefa_edit'),
    path('tarefa/deletar/<int:pk>', tarefa_delete, name='tarefa_delete'),
]