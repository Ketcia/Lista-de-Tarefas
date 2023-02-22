from django.urls import path
from .views import home,salvar,criarTarefa,editar, update, delete, verMais, atualiza_stt

urlpatterns = [
    path('', home),
    path('novatarefa/', criarTarefa, name="novatarefa"),
    path('salvar', salvar, name="salvar"),
    path('editar/<int:id>', editar, name="editar"),
    path('update/<int:id>', update, name="update"),
    path('delete/<int:id>', delete, name="delete"),
    path('detalhes/<int:id>', verMais, name="detalhes"),
    path('status/<int:id>', atualiza_stt, name="status"),
]
