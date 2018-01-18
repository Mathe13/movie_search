import sys
import requests
import json

def get_data_movie(movie_name,parametro):
    try:
        req=requests.get(url='http://www.omdbapi.com/?i=tt3896198&apikey=b34f7b7b&'+parametro+'='+movie_name+'&type=movie')
        return json.loads(req.text)
    except Exception as e:
        print('erro:',e)



def print_movie_data(movie_data):
    try:

        if movie_data['Response']=='False':
            print('filme não encontrado')
        else:
            print('====Movie data====')
            print('\tTitulo:',movie_data.get('Title'))
            print('\tAno:',movie_data.get('Year'))
            print('\tImdb:',movie_data.get('imdbRating'))
            print('\tProdutora',movie_data.get('Production'))
            print('\tSite:',movie_data.get('Website'))
            print('\tPlot:',movie_data.get('Plot'))

    except IndexError:
        print('you are missing the movie name')
        return
    except Exception as e:
        print('Erro:',e)




def main():
    op=str(sys.argv[1])
    if(len(sys.argv)<2):
        print("use: movie_search -op movie_name")
    else:
        if(op=='-s'):
            print('todo')
            resposta=get_data_movie(str(sys.argv[2:]),'s')
            print('existem',resposta.get('totalResults'),'resultado para sua busca')
            ver=input('deseja ver todos os resultados?(y/n)')
            if(ver=='y' or ver=='Y'):
                print('todo')
                for i in range(0,int(resposta.get('totalResults'))):
                    print('teste')
                    print_movie_data(resposta)
            else:
                print('todo')
        elif(op=='-t'):
            resposta=get_data_movie(str(sys.argv[2:]),'t')
            print_movie_data(resposta)
        else:
            print('opção desconhecida:use -t ou -s')




if (__name__=='__main__'):
    main()
else:
    print('execute este script diretamente')
