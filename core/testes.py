"""Arquivo para testar gambiarras."""
from omdbapi import omdbapi as omdb_api

if __name__ == '__main__':
    filme = omdb_api(movie_name='The matrix', parametro='t')
    filme.get_data()
    # print(filme.data)
    for k, v in filme.data.items():
        print("{} {}".format(k, v))
    print(filme)
    print(filme.get_key_data('r'))
