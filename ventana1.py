import sys

from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QHBoxLayout, QApplication, QFormLayout, QLineEdit, \
    QPushButton


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

        #creamos layout izquierdo
        self.ladoIzquierdo=QFormLayout()

        #creamos letrero
        self.letrero1=QLabel()

        #Escribimos texto del letrero
        self.letrero1.setText("Informacion del cliente")

        #Asignacion de tipo de letra
        self.letrero1.setFont(QFont("Andale Mono",20))

        #Color del texto
        self.letrero1.setStyleSheet("color:#000080;")

        #Agregreamos el letrero en la primera fila
        self.ladoIzquierdo.addRow(self.letrero1)

        #Hacemos el letrero 2
        self.letrero2=QLabel()

        #establecemos el tama;o del letrero
        self.letrero2.setFixedWidth(340)

        #Escribimos el texto del letrero
        self.letrero2.setText("Por favor ingrese la informacion del cliente"
                              "\nen el formulario de abajo los campos marcados"
                              "\ncon un asterisco son obligatorios")

        #tipo de letra letrero2
        self.letrero2.setFont(QFont("Andale Mono", 10))

        #ponemos color del texto y margenes
        self.letrero2.setStyleSheet("color:#000080; margin-bottom:40px;"
                                    "margin-top:20px;"
                                    "padding-bottom:10px;"
                                    "border:2px solid #000080;"
                                    "border-left:none;"
                                    "border-right:none;"
                                    "border-top:none;")
        #agregar letrero 2 a la fila
        self.ladoIzquierdo.addRow(self.letrero2)

        #hacemos el campo para ingresar el nombre
        self.nombreCompleto=QLineEdit()
        self.nombreCompleto.setFixedWidth(250)


        #Agregarmos estos al formulario
        self.ladoIzquierdo.addRow("Nombre Completo* :",self.nombreCompleto)

        #Campo de ingresar contrase;a
        self.password1=QLineEdit()
        self.password1.setFixedWidth(250)
        self.password1.setEchoMode(QLineEdit.Password)

        # Agregarmos estos al formulario
        self.ladoIzquierdo.addRow("Contraseña* :", self.password1)

        # Campo de ingresar contrase;a
        self.password2 = QLineEdit()
        self.password2.setFixedWidth(250)
        self.password2.setEchoMode(QLineEdit.Password)

        # Agregarmos estos al formulario
        self.ladoIzquierdo.addRow("Contraseña* :", self.password2)

        # hacemos el campo de documento
        self.documento = QLineEdit()
        self.documento.setFixedWidth(250)

        # Agregarmos estos al formulario
        self.ladoIzquierdo.addRow("Documento* :", self.documento)


        # hacemos el campo de Correo
        self.correo = QLineEdit()
        self.correo.setFixedWidth(250)

        # Agregarmos estos al formulario
        self.ladoIzquierdo.addRow("Correo* :", self.correo)

        #boton regristrar
        self.botonRegistrar=QPushButton("Registrar")

        #Establecemos el ancho del boton
        self.botonRegistrar.setFixedWidth(90)

        #estilos del boton
        self.botonRegistrar.setStyleSheet("background-color:#000080;"
                                          "color:#FFFFFF;"
                                          "padding:10px;"
                                          "margin-top:40px;")

        #conexion con el boton registrar
        #self.botonRegistrar.clicked.connect(self.accion_botonregistrar)

        #Hacemos el boton limpiar datos
        self.botonlimpiar = QPushButton("Limpiar")

        # Establecemos el ancho del boton
        self.botonlimpiar.setFixedWidth(90)

        # estilos del boton
        self.botonlimpiar.setStyleSheet("background-color:#000080;"
                                          "color:#FFFFFF;"
                                          "padding:10px;"
                                          "margin-top:40px;")
        #conexion con funcion limpiar
        #self.botonRegistrar.clicked.connect(self.accion_botonlimpiar)


        self.ladoIzquierdo.addRow(self.botonRegistrar,self.botonlimpiar)



        #Agregamos el layout al lado izquierdo al layout horizaontal
        self.horizontal.addLayout(self.ladoIzquierdo)


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