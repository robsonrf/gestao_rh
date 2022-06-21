from django.views.generic import (
    ListView,
    UpdateView,
    DeleteView,
    CreateView
)
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .models import Funcionario


class FuncionariosList(ListView):
    model = Funcionario

    # Dica: sobrescrevendo o metodo get_queryset pois o default retorna todos os registros
    # assim, pode-se alterar a regra com filtro por exemplo
    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Funcionario.objects.filter(empresa=empresa_logada)


class FuncionarioNovo(CreateView):
    model = Funcionario
    fields = ['nome', 'departamentos']  # fields: campos do form

    def form_valid(self, form):
        funcionario = form.save(commit=False) # nao salva ainda, objet só em memoria
        username = funcionario.nome.split(' ')[0] + funcionario.nome.split(' ')[1]
        funcionario.empresa = self.request.user.funcionario.empresa
        funcionario.user = User.objects.create(username=username)
        funcionario.save()
        return super(FuncionarioNovo, self).form_valid(form)


class FuncionarioEdit(UpdateView):
    model = Funcionario
    fields = ['nome', 'departamentos']


class FuncionarioDelete(DeleteView):
    model = Funcionario
    success_url = reverse_lazy('list_funcionarios')
