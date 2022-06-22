from django.db import models
from django.urls import reverse
from apps.funcionarios.models import Funcionario

class Documento(models.Model):
    descricao = models.CharField(max_length=100)
    pertence = models.ForeignKey(Funcionario, on_delete=models.PROTECT)
    arquivo = models.FileField(upload_to='documentos') # vai armazenar na pasta /media/documentos. Ver settings.py > MEDIA_ROOT

    def get_absolute_url(self):
        # retorna para o edit de funcionario ao qual o doc pertence
        return reverse('update_funcionario', args=[self.pertence.id])

    def __str__(self):
        return self.descricao
