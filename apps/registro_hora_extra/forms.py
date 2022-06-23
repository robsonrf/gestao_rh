from django.forms import ModelForm
from .models import RegistroHoraExtra
from apps.funcionarios.models import Funcionario


class RegistroHoraExtraForm(ModelForm):

    # sobrescreve o metodo init para fazer o filtro do funcionario pela empresa do usuario logado
    def __init__(self, user, *args, **kwargs):
        super(RegistroHoraExtraForm, self).__init__(*args, **kwargs)
        self.fields['funcionario'].queryset = Funcionario.objects.filter(
            empresa=user.funcionario.empresa)

    class Meta:
        model = RegistroHoraExtra
        fields = ['motivo', 'funcionario', 'horas']
