'''
Para a atividade desta semana, você deverá criar um interator que irá iterar os dados da API (Application Interface) da tabela FIPE e retornar os carros de uma determinada marca de veículos (essa deverá ser passada para a classe que fará o papel de interator no momento da instanciação, neste caso use o ID de uma marca).

Para trazer esses dados, será necessário interagir com a API da FIPE disponível nesse endereço: https://deividfortuna.github.io/fipe/. Dicas:

- Para listar as marcas use a URL:  https://parallelum.com.br/fipe/api/v1/carros/marcas dessa forma serão listadas todas as marcas que a API possui. Escolha uma para ser usada na próxima etapa, grave o ID dela para ser usado no seu código.

- Nesta etapa use a marca selecionada para poder retornar os veículos que essa marca possui usando a URL: https://parallelum.com.br/fipe/api/v1/carros/marcas/{ID_MARCASELECIONADA}/modelos
Ao chamar esse endpoint, será retornada uma resposta que possui um nó, no formato JSON, com os modelos dos veículos que ela possui.

- Seu interator deverá inteirar em cada um desses modelos e trazer informações do nome e ID do veículo da marca selecionada. 

'''

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

# Criação do iterador da tabela FIPE
class fipe_iterator:
    def __init__(self, marca_id):
        self.marca_id = marca_id
        self.modelos = self.get_modelos()
        self.index = 0

    def get_modelos(self):
        url = f'https://parallelum.com.br/fipe/api/v1/carros/marcas/{self.marca_id}/modelos'
        headers = {'user-agent': 'Pantoja'}
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            modelos = response.json().get('modelos', [])
            return modelos
        else:
            raise Exception(f"Ocorreu um erro ao obter os dados da API!")

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.modelos):
            modelo = self.modelos[self.index]
            self.index += 1
            veiculo_id = modelo.get('codigo')
            veiculo_nome = modelo.get('nome')
            return {'id': veiculo_id, 'nome': veiculo_nome}
        else:
            raise StopIteration

# Exemplo de uso do iterador para a marca com ID 171 (LAMBORGHINI)
marca_id_selecionada = 171
carro_iterator = fipe_iterator(marca_id_selecionada)

# Print dos nomes do carro referente a marca (ID 171)
for carro in carro_iterator:
    print(f"ID: {carro['id']}, Nome: {carro['nome']}")
