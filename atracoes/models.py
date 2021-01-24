from django.db import models

class Atracoes(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    horario = models.TextField()
    idade_min = models.IntegerField()

    def __srt__(self):
        return self.nome
        
