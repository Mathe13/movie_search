import sys
import requests
import json
#from Object import ClassName as Parent
class omdbapi():
    def __init__(self,movie_name,parametro,pagina):
        try:
            #variaveis pra gerar url
            # self.movie_name=movie_name
            # self.parametro=parametro
            # self.pagina=pagina
            self.url_base='http://www.omdbapi.com/?i=tt3896198&apikey=b34f7b7b&'
            self.url=self.url_base+parametro+'='+movie_name+'&type=movie&page='+pagina
            #print('init funfou')
            print(self.url)
        except:
            print('erro ao gerar url de consulta')

    def get_data(self):
        try:
            print('make_request')
            self.data=requests.get(self.url)
            #print(self.data.text)
            #print(self.url)
            self.data=json.loads(self.data.text)
            #print(self.data)
            return
            # if self.data['Response']=='False':
            #     print('filme não encontrado')
            #     sys.exit()
            # else:
            #     return resposta
        except:
            print('erro ao buscar filme:')
