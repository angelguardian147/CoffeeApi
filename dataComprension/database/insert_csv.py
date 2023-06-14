
from dataComprension.models import Cultivos
import pandas as pd


columns = ['c_d_dep', 'departamento', 'c_d_mun', 'municipio', 'grupo_de_cultivo',
       'subgrupo_de_cultivo', 'cultivo', 'desagregaci_n_regional_y', 'a_o',
       'periodo', 'rea_sembrada_ha', 'rea_cosechada_ha', 'producci_n_t',
       'rendimiento_t_ha', 'estado_fisico_produccion', 'nombre_cientifico',
       'ciclo_de_cultivo']

df = pd.read_csv('static/cultivos_rendimiento.csv')
df.columns = columns
df = df[df['cultivo'] == 'CAFE']


def insertCSV():
    for val in df.values:
        q = Cultivos(
            c_d_dep = val[0],
            departamento = val[1],
            c_d_mun = val[2],
            municipio = val[3],
            grupo_de_cultivo = val[4],
            subgrupo_de_cultivo = val[5],
            cultivo = val[6],
            desagregaci_n_regional_y = val[7],
            a_o = val[8],
            periodo = val[9],
            rea_sembrada_ha = val[10],
            rea_cosechada_ha = val[11],
            producci_n_t = val[12],
            rendimiento_t_ha = val[13],
            estado_fisico_produccion = val[14],
            nombre_cientifico = val[15],
            ciclo_de_cultivo = val[16]
        ) 
        q.save()