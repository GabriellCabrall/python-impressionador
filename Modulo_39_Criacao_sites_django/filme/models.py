from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.

LISTA_CATEGORIAS = (
    ('TRANSITO', 'Trânsito'),
    ('COMIDAS', 'Comidas'),
    ('RELATOS', 'Relatos'),
    ('JOGOS', 'Jogos'),
    ('FUTEBOL', 'Futebol'),
    ('OUTROS', 'Outros'),
)

# Criar o filme
class Filme(models.Model):
    titulo = models.CharField(max_length=200)
    thumb = models.ImageField(upload_to='thumb_filmes')
    descricao = models.TextField(max_length=10000)
    categoria = models.CharField(max_length=20, choices=LISTA_CATEGORIAS)
    visualizacoes = models.IntegerField(default=0)
    data_criacao = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo


# Criar os episódios
class Episodio(models.Model):
    filme = models.ForeignKey("Filme", related_name="episodios", on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    video = models.URLField()

    def __str__(self):
        return self.filme.titulo + " - " + self.titulo



# Criar os usuários
class Usuario(AbstractUser):
    filmes_vistos = models.ManyToManyField("Filme")