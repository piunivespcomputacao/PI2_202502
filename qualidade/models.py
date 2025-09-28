from django.db import models

class Compressor(models.Model):
    id = models.IntegerField(primary_key=True)
    rpm = models.FloatField()
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
    exvalve = models.IntegerField(default=0) # Use IntegerField com default 0
    acmotor = models.IntegerField(default=0) # Use IntegerField com default 0
    
    # Campos de Diagnóstico (Necessários para o Django, defina defaults)
    status_qualidade = models.CharField(max_length=20, default='Não analisado')
    diagnostico = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return f'Compressor ID: {self.id}'