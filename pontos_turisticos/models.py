from django.db import models
from atracoes.models import Atracoes
from comentarios.models import Comentario
from avaliacoes.models import Avaliacao
from endereco.models import Endereco

class PontosTuristicos(models.Model):
    
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)
    atracoes = models.ManyToManyField(Atracoes)
    comentarios = models.ManyToManyField(Comentario)
    Avaliacoes = models.ManyToManyField(Avaliacao)
    endereco = models.ForeignKey(Endereco,on_delete=models.CASCADE,blank=True,null=True)
    



    def __str__(self):
        return self.nome
    

