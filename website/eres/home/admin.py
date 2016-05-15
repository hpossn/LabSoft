from django.contrib import admin

from .  import models

admin.site.register(models.Usuario)
admin.site.register(models.Regiao)
admin.site.register(models.Destinatario)
admin.site.register(models.Recibo)
admin.site.register(models.Funcionario)
admin.site.register(models.Gerente)
admin.site.register(models.Entregador)
admin.site.register(models.Cliente)
admin.site.register(models.Entrega)
admin.site.register(models.Veiculo)
