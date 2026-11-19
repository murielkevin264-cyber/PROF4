
#David Achicanoy.
#  cracion clase abstracta y class Cliente encapsulacion de datos y validaciones 

from abc import ABC, abstractmethod  # Importa herramientas para crear clases abstractas- que No se instancia Directamente

#------------CLASEE ABSTRACTA - Clase Base-----------------------#
class EntidadGeneral(ABC): # Crea clase abstracta EntidadGeneral.(ABC) al heredar de ABC Puede contener metodos abstractos.

    def __init__(self, identificador): # define constructor de la clase abstracta. identifica cada entidad -como por EJ. Class Cliente.
        if not isinstance(identificador, str) or not identificador.strip(): # valida que el identificador sea cadena de texto y no este vacio. .strip() elimina espacios alinicio y final.
            raise TypeError("El identificador debe ser una cadena de texto no vacía.") #lanza excepcion  si no se cumple la condicion anterior,Si el valor no es texto o queda vacío
        self._identificador = identificador # almacena dato como atributo interno. El guion bajo "_" indica atributo privado-protegido.

    @property # permite acceso al identificador como propiedad, sin llamar un metodo.
    def identificador(self): # define la propiedady que expone el dato almacenado en identificador.
        return self._identificador # devuelve identificador privado

    @abstractmethod # para declarar a las clases hijas que deben implementarel metodo.
    def describir(self): # define metodo abstracto que describe la entidad.
        pass    # pass- es decir no tiene ninguna implementacion aqui.    

 
 # ------------------ Clase concreta (hija)---------------#
class Cliente(EntidadGeneral): # declara Cliente como clase hija hereda de EntidadGneral el identificador y debe implementar describir-
    #------------------ Validacion nombre--------------------------#
    @staticmethod #indica que el metodo de validacion pertenece a la clase, no necesita una instancia  -self
    def validar_nombre(nombre): # define metodo para validar nombre
        if not isinstance(nombre, str): # comprueba  que sea  cadena de texto Str.
            raise TypeError("Atencion. El nombre debe ser texto.") # mensaje de error al no ingresar texto Str.

        nombre = " ".join(nombre.split()) # elimina valida espacios al inicio y final. se separa las paabras.-con .join() se unen nuevamente usando un solo espacio.
        permitidos = {"-", "'", "’"} # conjunto de signos permitidos en nombre

        if not nombre or not any(c.isalpha() for c in nombre): # not nombre. para identificar cadena texto Str vacia. any() devuelve True si alguna caracter no es letra.
            raise ValueError("Atencion .El nombre debe contener letras.") # informa  la falta de letras.

        if any(
            not c.isalpha()  
              and not c.isspace() # para validar que el caracter no sea espacio
                and c not in permitidos
            for c in nombre
        ): # recorre y  revisa cada caracter detecta los que no sean letra, el espacio y signos permitidos.
            raise ValueError(" Atencion. El nombre contiene caracteres no permitidos.") #  indica tipo correcto pero si valor no cumple condicion ,lanza Error, caracteres no permitidos

        return nombre # retorna nombre validado.
# -------------------------------------Validacion Correo----------------------#
    @staticmethod # metodo indpendiente
    def validar_correo(correo): # funcion para validar correo electronico
        if not isinstance(correo, str): # confirma que se atexto.
            raise TypeError("Atencion. El correo debe ser texto.") # lanza error si no es texto.

        correo = correo.strip() # elimina espacios al inicio y final

        if any(c.isspace() for c in correo) or correo.count("@") != 1: # valida los espacios internos y que no hay mas de un @ en el dominio del correo
            raise ValueError("Atencion. El correo debe tener un solo @ y no contener espacios.")# lanza error si no cumple la condicion anterior

        usuario, dominio = correo.split("@") # separa el correo en anterior y posterior referente a el caracter @.

        if (not usuario or not dominio or ".." in usuario
                or usuario.startswith(".")
                or usuario.endswith(".")): # valida que las dos partes existan y que usuario no contenga puntos al inicio y final ni que los repita.
            raise ValueError("Atencion. El correo tiene un formato inválido.") # lanza error si no se cumple condicion anterior.

        partes_dominio = dominio.split(".") # divide el dominio del correo por puntos
        if len(partes_dominio) < 2: # valida que el dominio (correo)tenga minimo un punto
            raise ValueError("Atencion. El dominio debe incluir un punto, como correopersonal@dominio.com.") # error si no cumple la condicion anterior

        for parte in partes_dominio: # revisa cada segmento del dominio (correo).
            if (
                not parte
                or parte.startswith("-") # revisa segmentos que comienzan en guion.
                or parte.endswith("-")  # revisa segmentos que terminan en guion.
                or not all(c.isalnum() or c == "-" for c in parte) #revisa caracteres diferentes de letras  numeros o
            ):
                raise ValueError("Atencion. El dominio del correo tiene un formato inválido.") # lanza error si no cumple la condicion anterior

        return correo # devuelve el correo validado.
#-------------------------Validacion Numero Documento-----------------------#

    @staticmethod # esatablece metodo indpendiente.
    def validar_documento(numero_documento): #define validar documento, recibe el numero de documento como parametro

        numero_documento = numero_documento.strip() # elimina espacios al inicio y final

        if not 5 <= len(numero_documento) <= 20: # valida longitud entre 5 y 20 caracteres
            raise ValueError("Atencion. El documento debe tener entre 5 y 20 caracteres.")# lanza validacion longitud caracteres.

        if not all(c.isalnum() or c == "-" for c in numero_documento):# permite solo letras numeros guiones.
            raise ValueError("Atencion. El documento solo puede contener letras, números y guiones.")

        return numero_documento # retorna el numero de documento validado.

    def __init__(self, identificador, nombre, correo, numero_documento): #  define constructor de la clase Cliente.
        super().__init__(identificador) #super() ejecuta constructor de la Clase Base.  ejecuta validacion y almacenamiento definidos en la clse padre.
        
        self._nombre = self.validar_nombre(nombre) #  valida y almacena nombre 
        self._correo = self.validar_correo(correo) # valida y  almacena correo
        self._numero_documento = self.validar_documento(numero_documento) # valida y  almacena numero_documento

    @property # convierte metodo en propiedad, permite consultar dato si utilizar ().
    def nombre(self): # define la propiedad nombre en esta instancia
        return self._nombre # retorna el nombre guardado internamente

    @property
    def correo(self): # define la propiedad correo en esta instancia
        return self._correo # retorna el correo guardado internamente

    @property
    def numero_documento(self): # define la propiedad numero_documento en esta instancia
        return self._numero_documento # retorna el número de documento guardado internamente

    def describir(self): #  define metodo donde se observa  un descripcion del cliente.
        return f"Cliente: {self._nombre} Correo: {self._correo} - Documento: {self._numero_documento}" #  construye y retorna una cadena de texto que describe al cliente, incluyendo su nombre, correo y número de documento.
 
 
 #-------------------------- validacion bloque Try,para  clase  cliente------------#

    def crear_cliente(): # define crear
        try:  # inicio de bloque par crear cliente
            cliente = Cliente(
                "001",
                input("Nombre: "),
                input("Correo: "),
                input("Número de documento: ")
            ) # 001: como identificador, luego solicita que se ingrese nombre, correo, numero documento
        except TypeError as error: #  se ejecuta si ocurre un error de tipo de dato, si no se cumple la condicion de tipo de dato
             print(f"Tipo de dato inválido: {error}")    
        except ValueError as error:
            
            print(f"Valor inválido: {error}")    
        else: #se ejecuta si no ocurrio ninguna excepcion en el bloque try
            print("Cliente creado exitosamente.")   
            print(cliente.describir())  # Muestra la descripción del cliente creado
        finally:
            print("Validacion Finalizada") # se ejecuta siempre, haya ocurrido o no una excepción, para indicar que la validación ha finalizado.
 
Cliente.crear_cliente() # Llama a la función para crear un cliente y manejar excepciones.            
#------------------ fin de  commit-----------------------------#