import sys

from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QHBoxLayout, QApplication


class Ventana1 (QMainWindow):
    def __init__(self,parent=None):
        super(Ventana1,self).__init__(parent)
        #Titulo de la ventana
        self.setWindowTitle("Formulario de registro")

        #Poner icono
        self.setWindowIcon(QtGui.QIcon('imagenes/descarga.png'))

        #Establecer las propiedades de ancho y alto
        self.ancho=900
        self.alto=600

        #establecer tamma;o d ventana
        self.resize(self.ancho,self.alto)

        #hacer que la ventana se vea en el centro
        self.pantalla=self.frameGeometry()
        self.centro=QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())

        #fijar ventana a esas dimensiones
        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)

        #establecer fondo
        self.fondo=QLabel(self)

        #Definir la imagen de fondo
        self.imagenFondo=QPixmap('imagenes/descarga (1).jpg')

        #definir imagen como fondo
        self.fondo.setPixmap(self.imagenFondo)

        #Establecer modo para escalar la imagen
        self.fondo.setScaledContents(True)

        #hacemos que se adapte al tama;o de la imagen
        self.resize(self.imagenFondo.width(),self.imagenFondo.height())

        #Establecemos la ventana de fondo como ventana central
        self.setCentralWidget(self.fondo)

        #Establecemos la distribucion de los elementos en un layout horizontal
        self.horizontal=QHBoxLayout()

        #Le ponemos las margenes
        self.horizontal.setContentsMargins(30,30,30,30)


        #siempre tener al final

        #Indicamos que layout principal del fondo es el horizontal
        self.fondo.setLayout(self.horizontal)



if __name__ == '__main__':
    # creamos una aplicacion pyqt5
    app = QApplication(sys.argv)

    # creamos un objeto de tipo ventana1
    ventana1 = Ventana1()

    # indicamos que la ventana se vea
    ventana1.show()

    # indicamos que la ventana se deje cerrar
    sys.exit(app.exec_())