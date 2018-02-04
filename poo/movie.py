from omdbapi import omdbapi as omdb_api

class movie(omdb_api):
    def __init__(self,movie_name,parametro,pagina):
        super(__class__,self).__init__(movie_name,parametro,pagina)
        #self.data=omdb_api.get_data(self)
        super(__class__,self).get_data()


    def print_data(self):
        try:
            print('====Movie data====')

            self.print_dict_data(index='Title',msg='\tTitulo:')
            self.print_dict_data(index='Year',msg='\tAno:')
            self.print_dict_data(index='imdbRating',msg='\tImdb:')
            self.print_dict_data(index='Production',msg='\tProdutora:')
            self.print_dict_data(index='Website',msg='\tSite:')
            self.print_dict_data(index='Plot',msg='\tPlot:')
            #print('\tTitulo:',self.data.get('Title'))
            #print('\tAno:',self.data.get('Year'))
            #print('\tImdb:',self.data.get('imdbRating'))
            #print('\tProdutora',self.data.get('Production'))
            #print('\tSite:',self.data.get('Website'))
            #print('\tPlot:',self.data.get('Plot'))

        except IndexError:
            print('esqueceu o nome do filme')
            return
        except Exception as e:
            print('Erro:',e)

    def print_dict_data(self,index,msg):
        data=self.data.get(index)
        if data!=None:
            print(msg+' '+data)
            return
        else:
            return

filme=movie(movie_name='The matrix',parametro='t',pagina='1')
filme.print_data()
