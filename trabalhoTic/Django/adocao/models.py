from django.db import models
from django.contrib.auth.models import User

class Pessoa(models.Model):

    nome = models.CharField(max_length=50)
    cargo = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    telefone = models.CharField(max_length=100)
    tipoUsuario = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Setor(models.Model):

    nome = models.CharField(max_length=50)
    diretor = models.TextField(blank=True, null=True, verbose_name="Setor",
                               )

    def __str__(self):
        return self.nome + '-' + self.diretor


class Viajem(models.Model):

    solicitante = models.ForeignKey(
        Pessoa, on_delete=models.PROTECT, max_length=50)
    nomePassageiros = models.CharField(max_length=100)
    quantidadePassageiros = models.CharField(max_length=50)
    finalidade = models.CharField(max_length=100)
    roteiro = models.CharField(max_length=100)
    dataPartida = models.CharField(max_length=8)
    dataRetorno = models.CharField(max_length=8)

    def __str__(self):
        return self.dataPartida + ' - ' + self.nomePassageiros


class Veiculo(models.Model):

    categoria = models.CharField(max_length=50)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=50)
    ano = models.CharField(max_length=100)
    quilometragem = models.CharField(max_length=100)
    placa = models.CharField(max_length=8)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.categoria + ' - ' + self.marca


class PassagemAviao(models.Model):

    companhiaAereaPartida = models.CharField(max_length=50)
    numVooPartida = models.CharField(max_length=100)
    companhiaAereaChegada = models.CharField(max_length=50)
    numVooChegada = models.CharField(max_length=100)
    horaPartida = models.CharField(max_length=100)
    horaChegada = models.CharField(max_length=8)

    def __str__(self):
        return self.companhiaAereaPartida + ' - ' + self.numVooPartida


class Servidor(models.Model):
    Siape = models.CharField(max_length=50)

    def __str__(self):
        return self.Siape


class Motorista(models.Model):

    cnh = models.CharField(max_length=50)
    validade = models.CharField(max_length=50)

    def __str__(self):
        return self.cnh + '-' + self.validade
