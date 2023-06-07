
import requests
import pandas as pd


url_api = 'https://www.datos.gov.co/resource/2pnw-mmge.json'

df = pd.read_json(url_api, orient='records')
df = df[df['cultivo'] == 'CAFE']
    

def resumeStatistic(params={}):
    return df.describe().round(2).to_json()


def misingData():
    return df.isna().sum().to_json()