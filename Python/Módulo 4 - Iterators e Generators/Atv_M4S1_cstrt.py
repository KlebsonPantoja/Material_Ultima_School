# Importando a biblioteca requests
import requests

# API das marcas
url_marca = f'https://parallelum.com.br/fipe/api/v1/carros/marcas/'
headers = {'user-agent': 'Pantoja'}
# Fazendo a solicitação para a API
response = requests.get(url_marca,headers)
# Verificando se a solicitação foi bem sucedida
if response.status_code == 200:
    data_marca = response.json()
else:
    print("Ocorreu um erro ao obter os dados da API!")


# API do modelo  #171 #LAMBORGHINI 
url_modelos = ' https://parallelum.com.br/fipe/api/v1/carros/marcas/171/modelos'
headers = {'user-agent': 'Pantoja'}
# Fazendo a solicitação para a API do modelo
modelos = requests.get(url_modelos,headers)
# Verificando se a solicitação foi bem sucedida
if modelos.status_code == 200:
    data_modelos = modelos.json()
else:
    print("Ocorreu um erro ao obter os dados da API!")
