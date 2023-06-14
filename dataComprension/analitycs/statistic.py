
import requests
import pandas as pd
from ..database.insert_csv import insertCSV


# url_api = 'https://www.datos.gov.co/resource/2pnw-mmge.json'
# df = pd.read_json(url_api, orient='records')

columns = ['c_d_dep', 'departamento', 'c_d_mun', 'municipio', 'grupo_de_cultivo',
       'subgrupo_de_cultivo', 'cultivo', 'desagregaci_n_regional_y', 'a_o',
       'periodo', 'rea_sembrada_ha', 'rea_cosechada_ha', 'producci_n_t',
       'rendimiento_t_ha', 'estado_fisico_produccion', 'nombre_cientifico',
       'ciclo_de_cultivo']

df = pd.read_csv('static/cultivos_rendimiento.csv')
df.columns = columns
df = df[df['cultivo'] == 'CAFE']
    

def resumeStatistic():
    return df.describe().round(2).to_json()


def allDataInZero():
    df_zero = df[['c_d_dep', 'c_d_mun', 'a_o', 'rea_sembrada_ha', 'rea_cosechada_ha', 'producci_n_t', 'rendimiento_t_ha']]
    data_zero = df_zero == 0
    return data_zero.sum().to_json()


def misingData():
    return df.isna().sum().to_json()