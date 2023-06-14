from django.db import models

# Create your models here.

class Cultivos(models.Model):

    id = models.IntegerField(primary_key=True)
    c_d_dep = models.IntegerField()
    departamento = models.CharField(max_length=50)
    c_d_mun = models.IntegerField()
    municipio = models.CharField(max_length=50)
    grupo_de_cultivo = models.CharField(max_length=50)
    subgrupo_de_cultivo = models.CharField(max_length=50)
    cultivo = models.CharField(max_length=50)
    desagregaci_n_regional_y = models.CharField(max_length=50)
    a_o = models.IntegerField()
    periodo = models.CharField(max_length=50)
    rea_sembrada_ha = models.FloatField()
    rea_cosechada_ha = models.FloatField()
    producci_n_t = models.FloatField()
    rendimiento_t_ha = models.FloatField(null=True, blank=True, default=0)
    estado_fisico_produccion = models.CharField(max_length=50)
    nombre_cientifico = models.CharField(max_length=50)
    ciclo_de_cultivo = models.CharField(max_length=50)
