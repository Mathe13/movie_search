import sys
import requests
import json

def get_data_movie(movie_name,parametro,pagina=1):
    try:
        req=requests.get(url='http://www.omdbapi.com/?i=tt3896198&apikey=b34f7b7b&'+parametro+'='+movie_name+'&type=movie&page='+pagina)
        #print('http://www.omdbapi.com/?i=tt3896198&apikey=b34f7b7b&'+parametro+'='+movie_name+'&type=movie&page='+pagina)
        resposta=json.loads(req.text)
        if resposta['Response']=='False':
            print('filme não encontrado')
            sys.exit()
        else:
            return resposta
    except Exception as e:
        print('erro:',e)

def mostra_pagina(dados,movie_name):
    #resposta=get_data_movie(str(sys.argv[2:]),'s'+str(pagina),str(pagina))
    #print (type(dados))
    for i in dados.get('Search'):
        #print('teste')
        print_movie_data(i)


def print_movie_data(movie_data):
    try:
        print('====Movie data====')
        print('\tTitulo:',movie_data.get('Title'))
        print('\tAno:',movie_data.get('Year'))
        print('\tImdb:',movie_data.get('imdbRating'))
        print('\tProdutora',movie_data.get('Production'))
        print('\tSite:',movie_data.get('Website'))
        print('\tPlot:',movie_data.get('Plot'))

    except IndexError:
        print('esqueceu o nome do filme')
        return
    except Exception as e:
        print('Erro:',e)




def main():
    op=str(sys.argv[1])
    if(len(sys.argv)<2):
        print("use: movie_search -op movie_name")
    else:
        if(op=='-s'):
            resposta=get_data_movie(str(sys.argv[2:]),'s','1')
            numberOfPages=int(resposta.get('totalResults'))//9
            print('existem',resposta.get('totalResults'),'resultado para sua busca')
            ver=input('deseja ver os resultados?(y/n)')
            if(ver=='y' or ver=='Y'):
                for i in range(0,numberOfPages):
                    print (i)
                    pagina=i+1
                    resposta=get_data_movie(str(sys.argv[2:]),'s',str(pagina))
                    mostra_pagina(resposta,pagina)
                    continua=input('continue?(y,n)')
                    if(continua=='n' or continua=='n'):
                        sys.exit()
            else:
                print('ok,saindo...')
                sys.exit()
        elif(op=='-t'):
            resposta=get_data_movie(str(sys.argv[2:]),'t','1')
            print_movie_data(resposta)
        else:
            print('opção desconhecida:use -t ou -s')




if (__name__=='__main__'):
    main()
else:
    print('execute este script diretamente')
