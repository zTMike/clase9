import sys

from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QHBoxLayout, QApplication, QFormLayout, QLineEdit, \
    QPushButton, QDialog, QDialogButtonBox, QVBoxLayout


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


        #___________LADO IZQUIERDO_______________



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



        #hacemos el campo para ingresar el nombre
        self.usuario=QLineEdit()
        self.usuario.setFixedWidth(250)


        #Agregarmos estos al formulario
        self.ladoIzquierdo.addRow("Usuario* :",self.usuario)

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
        self.botonRegistrar.clicked.connect(self.accion_botonregistrar)

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
        self.botonlimpiar.clicked.connect(self.accion_botonlimpiar)


        self.ladoIzquierdo.addRow(self.botonRegistrar,self.botonlimpiar)

        #___________Fin Lado Izquierdo_____________


        #_______________Inicio Lado derecho____________
        # creamos layout Derecho
        self.ladoderecho = QFormLayout()

        # creamos letrero
        self.letrero1 = QLabel()

        # Escribimos texto del letrero
        self.letrero1.setText("Recuperar contraseña")

        # Asignacion de tipo de letra
        self.letrero1.setFont(QFont("Andale Mono", 20))

        # Color del texto
        self.letrero1.setStyleSheet("color:#000080;")

        # Agregreamos el letrero en la primera fila
        self.ladoderecho.addRow(self.letrero1)

        # Hacemos el letrero 2
        self.letrero2 = QLabel()

        # establecemos el tama;o del letrero
        self.letrero2.setFixedWidth(340)

        # Escribimos el texto del letrero
        self.letrero2.setText("Por favor ingrese la informacion para recuperar"
                              "\nla contraseña. los campos marcados"
                              "\ncon un asterisco son obligatorios")

        # tipo de letra letrero2
        self.letrero2.setFont(QFont("Andale Mono", 10))

        # ponemos color del texto y margenes
        self.letrero2.setStyleSheet("color:#000080; margin-bottom:40px;"
                                    "margin-top:20px;"
                                    "padding-bottom:10px;"
                                    "border:2px solid #000080;"
                                    "border-left:none;"
                                    "border-right:none;"
                                    "border-top:none;")
        # agregar letrero 2 a la fila
        self.ladoderecho.addRow(self.letrero2)


        #__Respuesta y pregunta vefificacion 1__
        # creamos letrero
        self.letrero3 = QLabel()
        # Escribimos texto del letrero
        self.letrero3.setText("Pregunta de verificacion 1*")
        #agregamos letrero a layout derecho
        self.ladoderecho.addRow(self.letrero3)

        # hacemos el campo para ingresar el nombre
        self.pregunta1 = QLineEdit()
        self.pregunta1.setFixedWidth(250)
        # Agregarmos estos al formulario
        self.ladoderecho.addRow(self.pregunta1)

        # creamos letrero
        self.letrero4 = QLabel()
        # Escribimos texto del letrero
        self.letrero4.setText("Respuesta de verificacion 1*")
        #agregamos letrero a layout derecho
        self.ladoderecho.addRow(self.letrero4)

        # hacemos el campo para ingresar el nombre
        self.respuesta1 = QLineEdit()
        self.respuesta1.setFixedWidth(250)
        # Agregarmos estos al formulario
        self.ladoderecho.addRow(self.respuesta1)

        # __Respuesta y pregunta vefificacion 2__

        # creamos letrero
        self.letrero4 = QLabel()
        # Escribimos texto del letrero
        self.letrero4.setText("Pregunta de verificacion 2*")
        # agregamos letrero a layout derecho
        self.ladoderecho.addRow(self.letrero4)

        # hacemos el campo para ingresar el nombre
        self.pregunta2 = QLineEdit()
        self.pregunta2.setFixedWidth(250)
        # Agregarmos estos al formulario
        self.ladoderecho.addRow(self.pregunta2)

        # creamos letrero
        self.letrero5 = QLabel()
        # Escribimos texto del letrero
        self.letrero5.setText("Respuesta de verificacion 2*")
        # agregamos letrero a layout derecho
        self.ladoderecho.addRow(self.letrero5)

        # hacemos el campo para ingresar el nombre
        self.respuesta2 = QLineEdit()
        self.respuesta2.setFixedWidth(250)
        # Agregarmos estos al formulario
        self.ladoderecho.addRow(self.respuesta2)

        # __Respuesta y pregunta vefificacion 3__

        # creamos letrero
        self.letrero6 = QLabel()
        # Escribimos texto del letrero
        self.letrero6.setText("Pregunta de verificacion 3*")
        # agregamos letrero a layout derecho
        self.ladoderecho.addRow(self.letrero6)

        # hacemos el campo para ingresar el nombre
        self.pregunta3 = QLineEdit()
        self.pregunta3.setFixedWidth(250)
        # Agregarmos estos al formulario
        self.ladoderecho.addRow(self.pregunta3)

        # creamos letrero
        self.letrero7 = QLabel()
        # Escribimos texto del letrero
        self.letrero7.setText("Respuesta de verificacion 3*")
        # agregamos letrero a layout derecho
        self.ladoderecho.addRow(self.letrero7)

        # hacemos el campo para ingresar el nombre
        self.respuesta3 = QLineEdit()
        self.respuesta3.setFixedWidth(250)
        # Agregarmos estos al formulario
        self.ladoderecho.addRow(self.respuesta3)

        # boton regristrar
        self.botonBuscar = QPushButton("Buscar")

        # Establecemos el ancho del boton
        self.botonBuscar.setFixedWidth(90)

        # estilos del boton
        self.botonBuscar.setStyleSheet("background-color:#000080;"
                                          "color:#FFFFFF;"
                                          "padding:10px;"
                                          "margin-top:40px;")

        # conexion con el boton registrar
        # self.botonBuscar.clicked.connect(self.accion_botonBuscar)

        # Hacemos el boton limpiar datos
        self.botonRecuperar = QPushButton("Recuperar")

        # Establecemos el ancho del boton
        self.botonRecuperar.setFixedWidth(90)

        # estilos del boton
        self.botonRecuperar.setStyleSheet("background-color:#000080;"
                                        "color:#FFFFFF;"
                                        "padding:10px;"
                                        "margin-top:40px;")
        # conexion con funcion limpiar
        #self.botonRecuperar.clicked.connect(self.accion_botonRecuperar)

        self.ladoderecho.addRow(self.botonBuscar, self.botonRecuperar)

        #_____________Fin  lado derecho___________

        #Agregamos el layout al lado izquierdo al layout horizaontal
        self.horizontal.addLayout(self.ladoIzquierdo)

        #Agregamos el layout al lado izquierdo al layout horizaontal
        self.horizontal.addLayout(self.ladoderecho)




        #siempre tener al final

        #Indicamos que layout principal del fondo es el horizontal
        self.fondo.setLayout(self.horizontal)

    def accion_botonlimpiar(self):
        self.nombreCompleto.setText("")
        self.usuario.setText("")
        self.documento.setText("")
        self.password1.setText("")
        self.password2.setText("")
        self.correo.setText("")
        self.pregunta1.setText("")
        self.pregunta2.setText("")
        self.pregunta3.setText("")
        self.respuesta1.setText("")
        self.respuesta2.setText("")
        self.respuesta3.setText("")


    def accion_botonregistrar(self):
        #creamos ventana de dialogo
        self.ventanaDialogo=QDialog(None, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint)

        #asignamos tama;o a la ventana de dailogo
        self.ventanaDialogo.resize(300,150)

        #Creamos el boton aceptar
        self.botonAceptar=QDialogButtonBox.Ok
        self.opciones=QDialogButtonBox(self.botonAceptar)
        self.opciones.accepted.connect(self.ventanaDialogo.accept)

        #Establecemos titulo de la ventana
        self.ventanaDialogo.setWindowTitle("Formulario registro")

        #Configuramos que la ventana sea modal
        self.ventanaDialogo.setWindowModality(Qt.ApplicationModal)



        #Creamos layout vertical
        self.vertical=QVBoxLayout()

        #Creamos en label para los mensajes
        self.mensaje=QLabel("")

        #estilo a los mensajes
        self.mensaje.setStyleSheet("background-color:#008845; color:#FFFFFF; padding:10px;")

        #agregamos mensajes al vertical
        self.vertical.addWidget(self.mensaje)

        # agregamos Boton al vertical
        self.vertical.addWidget(self.opciones)

        #asigna layout a la ventana
        self.ventanaDialogo.setLayout(self.vertical)



        #datos correctos
        self.datoscorrectos=True

        #Validar 2 contrase;as iguales

        if (self.password1.text() != self.password2.text()):
            self.datoscorrectos=False

            #cambiamos mensaje
            self.mensaje.setText("Las password no coinsiden")
            self.accion_botonlimpiar()
            self.ventanaDialogo.exec_()

        if (self.nombreCompleto.text()==''or
            self.usuario.text()==''or
            self.documento.text()==''or
            self.password1.text()==''or
            self.password2.text()==''or
            self.correo.text()==''or
            self.pregunta1.text()==''or
            self.pregunta2.text()==''or
            self.pregunta3.text()==''or
            self.respuesta1.text()==''or
            self.respuesta2.text()==''or
            self.respuesta3.text()==''
        ):
            self.datoscorrectos = False
            # cambiamos mensaje
            self.mensaje.setText("Debe ingresar todos los campos")
            self.accion_botonlimpiar()
            self.ventanaDialogo.exec_()

        if self.datoscorrectos:

            self.mensaje.setText("Datos guardados correctamente")

            self.ventanaDialogo.exec_()
            #abrimos el archivo en modo agregar
            self.file=open('datos/clientes.txt' , 'ab')

            #Traer el texto de los Qline y los concatena con ;
            self.file.write(bytes(
                self.nombreCompleto.text()+";"
                +self.usuario.text()+";"
                +self.documento.text()+";"
                +self.password1.text()+";"
                +self.password2.text()+";"
                +self.correo.text()+";"
                +self.pregunta1.text()+";"
                +self.pregunta2.text()+";"
                +self.pregunta3.text()+";"
                +self.respuesta1.text()+";"
                +self.respuesta2.text()+";"
                +self.respuesta3.text()+"\n", encoding='UTF-8'))
            self.file.close()

            #abrimos en modo lectura en formato bite
            self.file=open('datos\clientes.txt','rb')

            #recorrer el archivo linea x linea
            while self.file:
                linea=self.file.readline().decode('UTF-8')
                print(linea)
                if linea=='':
                    break
            self.file.close()
            self.accion_botonlimpiar()























if __name__ == '__main__':
    # creamos una aplicacion pyqt5
    app = QApplication(sys.argv)

    # creamos un objeto de tipo ventana1
    ventana1 = Ventana1()

    # indicamos que la ventana se vea
    ventana1.show()

    # indicamos que la ventana se deje cerrar
    sys.exit(app.exec_())