from django.views.generic import (
    ListView,
    UpdateView,
    DeleteView,
    CreateView
)
from django.urls import reverse_lazy
from .models import RegistroHoraExtra
from .forms import RegistroHoraExtraForm


class HoraExtraList(ListView):
    model = RegistroHoraExtra


    # Dica: sobrescrevendo o metodo get_queryset pois o default retorna todos os registros
    # assim, pode-se alterar a regra com filtro por exemplo
    # funcionario__empresa
    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return RegistroHoraExtra.objects.filter(funcionario__empresa=empresa_logada)


class HoraExtraEdit(UpdateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm
    # Define um Form customizado - para filtrar os funcionarios inves de trazer todos

    # esse metodo recupera (injeta) o 'user' que será utilizado no método init do forms.py
    def get_form_kwargs(self):
        kwargs = super(HoraExtraEdit, self).get_form_kwargs()
        # adiciona o usuario no kwargs
        kwargs.update({'user': self.request.user})
        return kwargs


class HoraExtraEditBase(UpdateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm
    # success_url = reverse_lazy('update_hora_extra_base') # manter essa linha caso queira volta pra listagem, e comentar get_success_url

    def get_success_url(self):
        return reverse_lazy('update_hora_extra_base', args=[self.object.id]) # para permanecer na tela de edição


    # esse metodo recupera (injeta) o 'user' que será utilizado no método init do forms.py
    def get_form_kwargs(self):
        kwargs = super(HoraExtraEditBase, self).get_form_kwargs()
        # adiciona o usuario no kwargs
        kwargs.update({'user': self.request.user})
        return kwargs


class HoraExtraDelete(DeleteView):
    model = RegistroHoraExtra
    success_url = reverse_lazy('list_hora_extra')

class HoraExtraNovo(CreateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm
    # Define um Form customizado - para filtrar os funcionarios inves de trazer todos


    # esse metodo recupera (injeta) o 'user' que será utilizado no método init do forms.py
    def get_form_kwargs(self):
        kwargs = super(HoraExtraNovo, self).get_form_kwargs()
        # adiciona o usuario no kwargs
        kwargs.update({'user': self.request.user})
        return kwargs
