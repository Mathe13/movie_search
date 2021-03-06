"""Main do projeto."""
# -*- coding: utf-8 -*-
import sys
import requests
from core import omdbapi as omdb_api
# from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.uic import loadUi


class movie_search(QMainWindow):
    """Classe principal."""

    def __init__(self):
        """Iniciar a interface."""
        super(movie_search, self).__init__()
        self.buscador = omdb_api.omdbapi()
        loadUi('gui/mainwindow.ui', self, resource_suffix='resources.qrc')
        self.poster.setPixmap(QPixmap('gui/imgs/poster_none.png'))
        self.setWindowTitle('Movie search')

        self.buscar.clicked.connect(self.buscar_info)

    def buscar_info(self):
        """Busca as informações."""
        # movie_name = self.barra_de_busca.text()

        self.dados = self.buscador.get_data(
            movie_name=self.barra_de_busca.text(), parametro='t')
        self.exibe_resposta()

    def exibe_resposta(self):
        """Coloca as respostas nos labels."""
        self.titulo.setText(self.buscador.get_resposta('Title', 'Título:'))
        self.ano.setText(self.buscador.get_resposta('Year', 'Ano:'))
        self.produtor.setText(
            self.buscador.get_resposta('Production', 'Produtor:'))
        self.diretor.setText(
            self.buscador.get_resposta('Director', 'Diretor:'))
        self.premios.setText(self.buscador.get_resposta('Awards', 'Premios:'))
        self.rank.setText(
            self.buscador.get_resposta('imdbRating', 'Rank IMDB:'))
        self.plot.setText(self.buscador.get_resposta('Plot', 'Plot:'))
        poster_data = requests.get(self.dados['Poster'])
        if (poster_data.content):
            poster = QImage()
            poster.loadFromData(poster_data.content)
            self.poster.setPixmap(QPixmap(poster))
        # quebra de linha:
        self.plot.setWordWrap(True)
        self.premios.setWordWrap(True)


app = QApplication(sys.argv)
widget = movie_search()
widget.show()
sys.exit(app.exec_())
