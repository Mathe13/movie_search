"""Classe para se conectar com a api omdb."""
import requests
import json


# from Object import ClassName as Parent
class omdbapi():
    """Classe para se conectar com a api omdb."""

    def __init__(self):
        """Inicializador, seta a url base."""
        self.url_base = (
            'http://www.omdbapi.com/?i=tt3896198&apikey=b34f7b7b&')

    def get_data(self, movie_name, parametro, pagina='1'):
        """função para buscar os dados da api."""
        try:
            url = (self.url_base + parametro + '=' + movie_name +
                   '&type=movie&page=' + pagina)
            print(url)
            print('make_request')
            data = requests.get(url)
            # print(self.data.text)
            # print(self.url)
            # self.data = json.loads(self.data.text)
            self.data = json.loads(data.text)
            # print(self.data)
            print('Buscou os dados')
            return self.data
            # if self.data['Response']=='False':
            #     print('filme não encontrado')
            #     sys.exit()
            # else:
            #     return resposta
        except Exception as e:
            print('erro ao buscar filme:', e)

    def get_resposta(self, chave, desc):
        """Se a chave n exitir retorna none para ser exibido."""
        print('Buscando a chave:' + chave)
        if chave in self.data:
            resposta = self.data[chave]
        else:
            resposta = "None"

        return ('<html><head/><body><p><span style=" font-size:14pt;">' +
                desc + resposta + '</span > </p > </body > </html >')
