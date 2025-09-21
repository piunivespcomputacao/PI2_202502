from django.db import models # Importa a classe principal do Django para modelos.

class Compressor(models.Model): # Cria a classe Compressor, que herda as funcionalidades de modelo do Django.
    id = models.IntegerField(primary_key=True) # Define um campo de número inteiro que será a chave primária da tabela.
    rpm = models.FloatField() # Define um campo para números com casas decimais, ideal para rotações.
    # Repete a lógica para todos os outros campos do seu dataset...
    motor_power = models.FloatField()
    outlet_pressure_bar = models.FloatField()
    air_flow = models.FloatField()
    noise_db = models.FloatField()
    outlet_temp = models.FloatField()
    gaccx = models.FloatField()
    gaccy = models.FloatField()
    gaccz = models.FloatField()
    haccx = models.FloatField()
    haccy = models.FloatField()
    haccz = models.FloatField()
    exvalve = models.FloatField()
    acmotor = models.FloatField()
    status_qualidade = models.CharField(max_length=50) # Cria um campo de texto para o status (APROVADO/REPROVADO).
    diagnostico = models.CharField(max_length=200) # Cria um campo de texto para o diagnóstico detalhado.

    def __str__(self): # Um método que define a representação em string do objeto.
        return f'Compressor ID: {self.id}' # Retorna o ID do compressor para fácil identificação no painel de admin.