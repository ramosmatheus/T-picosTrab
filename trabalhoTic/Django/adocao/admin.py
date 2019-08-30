from django.contrib import admin

from .models import Pessoa, Servidor, Setor, Veiculo, Viajem, Motorista, PassagemAviao

# Register your models here.
admin.site.register(Pessoa)
admin.site.register(Servidor)
admin.site.register(Setor)
admin.site.register(Viajem)
admin.site.register(Veiculo)
admin.site.register(Motorista)
admin.site.register(PassagemAviao)