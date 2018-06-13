from django.db import models

# Create your models here.

class Message(models.Model):
    name = models.CharField('Nome', max_length=100)
    email = models.CharField('Email', max_length=64)
    message = models.TextField('Mensagem')

    created = models.DateTimeField('Criado em', auto_now_add=True)

    class Meta:
        verbose_name = 'Mensagem'
        verbose_name_plural = 'Mensagens'
        ordering = ['-created']

    def __str__(self):
        return self.name
