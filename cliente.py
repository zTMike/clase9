class Clientes:
    def __init__(self,nombrecompleto,
                 usuario,
                 documento,
                 password,
                 password1,
                 correo,
                 pregunta1,
                 pregunta2,
                 pregunta3,
                 respuesta1,
                 respuesta2,
                 respuesta3,
                 ):
        self.nombreCompleto=nombrecompleto
        self.usuario=usuario
        self.password=password
        self.password1= password1
        self.documento=documento
        self.correo=correo
        self.pregunta1=pregunta1
        self.respuesta1=respuesta1
        self.pregunta2=pregunta2
        self.respuesta2=respuesta2
        self.pregunta3=pregunta3
        self.respuesta3=respuesta3


    def __str__(self):
        return f"Nombre {self.nombreCompleto} documento {self.documento}"

