
#David Achicanoy. cracion clase abstracta y class Cliente encapsulacion de datos y validaciones 

from abc import ABC, abstractmethod  # Importa herramientas para crear clases abstracats


class EntidadGeneral(ABC): # declara clase abstracta EntidadGeneral.
    def __init__(self, identificador): # define constructor de la clase abstracta.
        if not isinstance(identificador, str) or not identificador.strip(): # valida que el identificador sea cadena de texto y no este vacio.
            raise TypeError("El identificador debe ser una cadena de texto no vacía.") #lanza excepcion  si no se cumple la condixion anterior
        self._identificador = identificador # alamacena dato como atributo interno.

    @property # permite acceso al identificador como propiedad, sin llamar un metodo.
    def identificador(self): # define la propiedady que expone el dato almacenado en identificador.
        return self._identificador # devuelve identificador privado

    @abstractmethod # para declarar a las clases hijas que deben implementarel metodo.
    def describir(self): # define metodo abstracto que describe la entidad.
        pass        

 
 # ------------------ Clase concreta (hija)---------------#
class Cliente(EntidadGeneral): # declara Cliente como calse hija hereda de EntidadGneral el identificador y debe implementar describir-
    
    @staticmethod #indica que el metodo de validacion pertenece a la clase, no necesita una instancia  -self
    def validar_nombre(nombre): # define metodo para validar nombre
        if not isinstance(nombre, str): # comprueba  que sea texto
            raise TypeError("Atencion. El nombre debe ser texto.") # mensaje de error al no ingresar texto str

        nombre = " ".join(nombre.split()) # elimina valida espacios al inicio y final.
        permitidos = {"-", "'", "’"} # conjunto de signos permitidos en nombre

        if not nombre or not any(c.isalpha() for c in nombre): # rechaza nombre vacio o sin letras
            raise ValueError("Atencion .El nombre debe contener letras.") # informa  la falta de letras.

        if any(
            not c.isalpha() and not c.isspace() and c not in permitidos
            for c in nombre
        ): # revisa cada caracter detecta los que no sean letra, el espacio y signos permitidos.
            raise ValueError(" Atencion. El nombre contiene caracteres no permitidos.") # lanza Error, caracteres no permitidos

        return nombre # retorna nombre validado.

    @staticmethod # metodo indpendiente
    def validar_correo(correo): # funcion para validar correo electronico
        if not isinstance(correo, str): # confirma que se atexto.
            raise TypeError("Atencion. El correo debe ser texto.") # lanza error si no es texto.

        correo = correo.strip() # elimina espacios al inicio y final

        if any(c.isspace() for c in correo) or correo.count("@") != 1: # valida los espacios internos y que no hay mas de un @ en el dominio del correo
            raise ValueError("Atencion. El correo debe tener un solo @ y no contener espacios.")# lanza error si no cumple la condicion anterior

        usuario, dominio = correo.split("@") # separa el correo en anterior y posterior referente a el caracter @.

        if (not usuario or not dominio or ".." in usuario
                or usuario.startswith(".") or usuario.endswith(".")): # valida que las dos partes existan y que usuario no contenga puntos al inicio y final ni que los repita.
            raise ValueError("Atencion. El correo tiene un formato inválido.")

        partes_dominio = dominio.split(".") # divide el dominio del correo por puntos
        if len(partes_dominio) < 2: # valida que el dominio (correo)tenga minimo un punto
            raise ValueError("Atencion. El dominio debe incluir un punto, como correopersonal@dominio.com.") # error si no cumple la condicion anterior

        for parte in partes_dominio: # revisa cada segmento del dominio (correo).
            if (
                not parte
                or parte.startswith("-")
                or parte.endswith("-")
                or not all(c.isalnum() or c == "-" for c in parte)
            ):
                raise ValueError("Atencion. El dominio del correo tiene un formato inválido.") # lanza error si no cumple la condicion anterior

        return correo # devuelve el correo validado.

    @staticmethod #metodod indpendiente
    def validar_documento(numero_documento): #define validar documento, recibe el numero de documento como parametro

        numero_documento = numero_documento.strip() # elimina espacios al inicio y final

        if not 5 <= len(numero_documento) <= 20: # valida longitud entre 5 y 20 caracteres
            raise ValueError("Atencion. El documento debe tener entre 5 y 20 caracteres.")# lanza validacion longitud caracteres.

        if not all(c.isalnum() or c == "-" for c in numero_documento):# permite solo letras numeros guiones.
            raise ValueError("Atencion. El documento solo puede contener letras, números y guiones.")

        return numero_documento # retorna el numero de documento validado.

    def __init__(self, identificador, nombre, correo, numero_documento): #  define constructor de la clase Cliente.
        super().__init__(identificador) #  ejecuta validacion y almacenamiento definidos en la clse padre.
        
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
        except TypeError as error: # error de tipo de dato, si no se cumple la condicion de tipo de dato
             print(f"Tipo de dato inválido: {error}")    
        except ValueError as error:
            
            print(f"Valor inválido: {error}")    
        else: #se ejecuta si no ocurrio ninguna excepcion en el bloque try
            print("Cliente creado exitosamente.")   
            print(cliente.describir())  # Muestra la descripción del cliente creado
        finally:
            print("Validacion Finalizada")

#------------------ end commit-----------------------------#



#Aporte kevin Muriel
# SEGUNDA PARTE: GESTION DE SERVICIOS

# Clase abstracta Servicio
class Servicio(EntidadGeneral):

    def __init__(self, identificador, nombre, precio_base):
        super().__init__(identificador)

        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre del servicio no puede estar vacio.")

        if not isinstance(precio_base, (int, float)) or isinstance(precio_base, bool) or precio_base <= 0:
            raise ValueError("El precio debe ser un numero mayor que cero.")

        self._nombre = nombre.strip()
        self._precio_base = precio_base

    @property
    def nombre(self):
        return self._nombre

    @property
    def precio_base(self):
        return self._precio_base

    # Metodo para calcular el costo con impuestos y descuentos
    def calcular_total(self, duracion, impuesto=0, descuento=0):

        if not isinstance(duracion, (int, float)) or isinstance(duracion, bool) or duracion <= 0:
            raise ValueError("La duracion debe ser mayor que cero.")

        if isinstance(impuesto, bool) or not isinstance(impuesto, (int, float)) or not 0 <= impuesto <= 100:
            raise ValueError("El impuesto debe estar entre 0 y 100.")

        if isinstance(descuento, bool) or not isinstance(descuento, (int, float)) or not 0 <= descuento <= 100:
            raise ValueError("El descuento debe estar entre 0 y 100.")

        subtotal = self._precio_base * duracion
        valor_descuento = subtotal * (descuento / 100)
        subtotal = subtotal - valor_descuento

        valor_impuesto = subtotal * (impuesto / 100)
        total = subtotal + valor_impuesto

        return total

    # Metodos abstractos que deben implementar las clases hijas
    @abstractmethod
    def validar_parametros(self, parametro):
        pass

    @abstractmethod
    def calcular_costo(self, duracion):
        pass

    @abstractmethod
    def describir(self):
        pass



# CLASE 1: RESERVA DE SALAS


class ReservaSala(Servicio):

    def __init__(self, identificador, nombre, precio_base, capacidad_maxima):
        super().__init__(identificador, nombre, precio_base)

        if not isinstance(capacidad_maxima, int) or isinstance(capacidad_maxima, bool) or capacidad_maxima <= 0:
            raise ValueError("La capacidad debe ser un numero entero positivo.")

        self._capacidad_maxima = capacidad_maxima

    def validar_parametros(self, cantidad_personas):

        if not isinstance(cantidad_personas, int) or isinstance(cantidad_personas, bool):
            raise TypeError("La cantidad de personas debe ser un numero entero.")

        if cantidad_personas <= 0:
            raise ValueError("Debe existir al menos una persona.")

        if cantidad_personas > self._capacidad_maxima:
            raise ValueError("La sala no tiene capacidad suficiente.")

        return True

    def calcular_costo(self, duracion):
        return self.calcular_total(duracion)

    def describir(self):
        return f"Servicio: {self._nombre} - Precio por hora: ${self._precio_base} - Capacidad: {self._capacidad_maxima} personas"



# CLASE 2: ALQUILER DE EQUIPOS

class AlquilerEquipo(Servicio):

    def __init__(self, identificador, nombre, precio_base, cantidad_disponible):
        super().__init__(identificador, nombre, precio_base)

        if not isinstance(cantidad_disponible, int) or isinstance(cantidad_disponible, bool) or cantidad_disponible < 0:
            raise ValueError("La cantidad disponible no puede ser negativa.")

        self._cantidad_disponible = cantidad_disponible

    def validar_parametros(self, cantidad_equipos):

        if not isinstance(cantidad_equipos, int) or isinstance(cantidad_equipos, bool):
            raise TypeError("La cantidad de equipos debe ser un numero entero.")

        if cantidad_equipos <= 0:
            raise ValueError("Debe solicitar al menos un equipo.")

        if cantidad_equipos > self._cantidad_disponible:
            raise ValueError("No hay suficientes equipos disponibles.")

        return True

    def calcular_costo(self, duracion):
        return self.calcular_total(duracion)

    def describir(self):
        return f"Servicio: {self._nombre} - Precio por dia: ${self._precio_base} - Equipos disponibles: {self._cantidad_disponible}"



# CLASE 3: ASESORIAS ESPECIALIZADAS


class AsesoriaEspecializada(Servicio):

    def __init__(self, identificador, nombre, precio_base, especialidad):
        super().__init__(identificador, nombre, precio_base)

        if not isinstance(especialidad, str) or not especialidad.strip():
            raise ValueError("Debe ingresar una especialidad valida.")

        self._especialidad = especialidad.strip()

    def validar_parametros(self, tema):

        if not isinstance(tema, str):
            raise TypeError("El tema de la asesoria debe ser texto.")

        if not tema.strip():
            raise ValueError("Debe ingresar el tema de la asesoria.")

        return True

    def calcular_costo(self, duracion):
        return self.calcular_total(duracion)

    def describir(self):
        return f"Servicio: {self._nombre} - Precio por hora: ${self._precio_base} - Especialidad: {self._especialidad}"



# FIN DE LA SEGUNDA PARTE


#Aporte Laura Ramos

# TERCERA PARTE: EXCEPCIONES PERSONALIZADAS Y GESTION DE RESERVAS

import logging
import os
from datetime import datetime

# 1. CONFIGURACION DEL ARCHIVO DE REGISTROS (LOGS)

RUTA_LOG = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "software_fj.log"
)

logging.basicConfig(
    filename=RUTA_LOG,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    encoding="utf-8"
)

logger = logging.getLogger("SoftwareFJ")

# 2. EXCEPCIONES PERSONALIZADAS

class ErrorSoftwareFJ(Exception):
    """Excepcion base del sistema Software FJ."""
    pass


class ClienteNoRegistradoError(ErrorSoftwareFJ):
    """Se genera cuando un cliente no esta registrado."""
    pass


class ServicioNoDisponibleError(ErrorSoftwareFJ):
    """Se genera cuando un servicio no esta disponible."""
    pass


class ReservaNoPermitidaError(ErrorSoftwareFJ):
    """Se genera cuando una operacion de reserva no esta permitida."""
    pass


class ErrorProcesamientoReserva(ErrorSoftwareFJ):
    """Se genera cuando ocurre un error al procesar una reserva."""
    pass

# 3. CONTROL DE DISPONIBILIDAD DE EQUIPOS

def _reservar_equipos(self, cantidad):
    self.validar_parametros(cantidad)
    self._cantidad_disponible -= cantidad

    logger.info(
        "Se reservaron %s unidades del servicio %s",
        cantidad,
        self.identificador
    )


def _liberar_equipos(self, cantidad):
    self._cantidad_disponible += cantidad

    logger.info(
        "Se liberaron %s unidades del servicio %s",
        cantidad,
        self.identificador
    )


# Se agregan los metodos a la clase AlquilerEquipo

AlquilerEquipo.reservar_equipos = _reservar_equipos
AlquilerEquipo.liberar_equipos = _liberar_equipos


# 4. CLASE RESERVA

class Reserva(EntidadGeneral):

    # Estados posibles de una reserva
    PENDIENTE = "Pendiente"
    CONFIRMADA = "Confirmada"
    CANCELADA = "Cancelada"

    def __init__(
        self,
        identificador,
        cliente,
        servicio,
        duracion,
        parametro,
        impuesto=0,
        descuento=0
    ):

        super().__init__(identificador)

        # Validacion del cliente
        if not isinstance(cliente, Cliente):
            raise TypeError(
                "La reserva debe estar asociada a un cliente valido."
            )

        # Validacion del servicio
        if not isinstance(servicio, Servicio):
            raise TypeError(
                "La reserva debe estar asociada a un servicio valido."
            )

        # Validacion de duracion
        if (
            isinstance(duracion, bool)
            or not isinstance(duracion, (int, float))
            or duracion <= 0
        ):
            raise ValueError(
                "La duracion debe ser un numero mayor que cero."
            )

        # Validacion de impuesto
        if (
            isinstance(impuesto, bool)
            or not isinstance(impuesto, (int, float))
            or not 0 <= impuesto <= 100
        ):
            raise ValueError(
                "El impuesto debe estar entre 0 y 100."
            )

        # Validacion de descuento
        if (
            isinstance(descuento, bool)
            or not isinstance(descuento, (int, float))
            or not 0 <= descuento <= 100
        ):
            raise ValueError(
                "El descuento debe estar entre 0 y 100."
            )

        self._cliente = cliente
        self._servicio = servicio
        self._duracion = duracion
        self._parametro = parametro
        self._impuesto = impuesto
        self._descuento = descuento

        self._estado = self.PENDIENTE
        self._costo_total = 0
        self._fecha_creacion = datetime.now()
        self._recursos_descontados = False

        logger.info(
            "Reserva %s creada para el cliente %s",
            identificador,
            cliente.identificador
        )

    # Propiedades para consultar los atributos

    @property
    def cliente(self):
        return self._cliente

    @property
    def servicio(self):
        return self._servicio

    @property
    def estado(self):
        return self._estado

    @property
    def costo_total(self):
        return self._costo_total

    # Metodo para confirmar una reserva

    def confirmar(self):

        if self._estado != self.PENDIENTE:
            raise ReservaNoPermitidaError(
                "Solo se pueden confirmar reservas pendientes."
            )

        try:

            # Validar los parametros del servicio
            self._servicio.validar_parametros(self._parametro)

            # Descontar equipos cuando corresponda
            if isinstance(self._servicio, AlquilerEquipo):

                self._servicio.reservar_equipos(self._parametro)
                self._recursos_descontados = True

            # Calcular el costo con impuesto y descuento
            self._costo_total = self._servicio.calcular_total(
                self._duracion,
                self._impuesto,
                self._descuento
            )

            if self._costo_total <= 0:
                raise ArithmeticError(
                    "El calculo del costo produjo un valor inconsistente."
                )

            self._estado = self.CONFIRMADA

            logger.info(
                "Reserva %s confirmada. Total: %.2f",
                self.identificador,
                self._costo_total
            )

            return self._costo_total

        except Exception as error:

            # Si ocurre un error, devolver los equipos descontados
            if self._recursos_descontados:

                self._servicio.liberar_equipos(self._parametro)
                self._recursos_descontados = False

            logger.exception(
                "Error al confirmar la reserva %s",
                self.identificador
            )

            # Encadenamiento de excepciones
            raise ErrorProcesamientoReserva(
                f"No fue posible confirmar la reserva "
                f"{self.identificador}: {error}"
            ) from error

    # Metodo para cancelar una reserva

    def cancelar(self):

        if self._estado == self.CANCELADA:
            raise ReservaNoPermitidaError(
                "La reserva ya se encuentra cancelada."
            )

        # Liberar equipos si la reserva estaba confirmada
        if (
            self._estado == self.CONFIRMADA
            and self._recursos_descontados
        ):

            self._servicio.liberar_equipos(self._parametro)
            self._recursos_descontados = False

        self._estado = self.CANCELADA

        logger.info(
            "Reserva %s cancelada",
            self.identificador
        )

        return True

    # Metodo para procesar la reserva

    def procesar(self):

        try:

            total = self.confirmar()

        except ErrorProcesamientoReserva as error:

            print(
                f"Error controlado al procesar reserva: {error}"
            )

            logger.error(
                "La reserva %s no pudo procesarse",
                self.identificador
            )

            raise

        else:

            print(
                f"Reserva {self.identificador} procesada correctamente. "
                f"Total: ${total:,.2f}"
            )

            return total

        finally:

            print(
                f"Finalizo el intento de procesamiento "
                f"de la reserva {self.identificador}."
            )

    # Metodo para describir la reserva

    def describir(self):

        return (
            f"Reserva {self.identificador} | "
            f"Cliente: {self._cliente.nombre} | "
            f"Servicio: {self._servicio.nombre} | "
            f"Duracion: {self._duracion} | "
            f"Estado: {self._estado} | "
            f"Total: ${self._costo_total:,.2f}"
        )


# 5. CLASE GESTOR DEL SISTEMA SOFTWARE FJ

class GestorSoftwareFJ:

    def __init__(self):

        self._clientes = []
        self._servicios = []
        self._reservas = []

    # Registrar clientes

    def registrar_cliente(self, cliente):

        if not isinstance(cliente, Cliente):
            raise TypeError(
                "Solo se pueden registrar objetos de tipo Cliente."
            )

        if any(
            c.numero_documento == cliente.numero_documento
            for c in self._clientes
        ):
            raise ValueError(
                "Ya existe un cliente con ese numero de documento."
            )

        self._clientes.append(cliente)

        logger.info(
            "Cliente registrado: %s",
            cliente.identificador
        )

        return cliente

    # Registrar servicios

    def registrar_servicio(self, servicio):

        if not isinstance(servicio, Servicio):
            raise TypeError(
                "El objeto ingresado no es un servicio valido."
            )

        if any(
            s.identificador == servicio.identificador
            for s in self._servicios
        ):
            raise ValueError(
                "Ya existe un servicio con ese identificador."
            )

        self._servicios.append(servicio)

        logger.info(
            "Servicio registrado: %s",
            servicio.identificador
        )

        return servicio

    # Crear reservas

    def crear_reserva(
        self,
        identificador,
        cliente,
        servicio,
        duracion,
        parametro,
        impuesto=0,
        descuento=0
    ):

        if cliente not in self._clientes:
            raise ClienteNoRegistradoError(
                "El cliente debe registrarse antes de reservar."
            )

        if servicio not in self._servicios:
            raise ServicioNoDisponibleError(
                "El servicio no esta registrado o disponible."
            )

        if any(
            r.identificador == identificador
            for r in self._reservas
        ):
            raise ValueError(
                "Ya existe una reserva con ese identificador."
            )

        reserva = Reserva(
            identificador,
            cliente,
            servicio,
            duracion,
            parametro,
            impuesto,
            descuento
        )

        self._reservas.append(reserva)

        logger.info(
            "Reserva %s agregada al gestor",
            identificador
        )

        return reserva

    # Consultar todas las reservas

    def listar_reservas(self):

        return [
            reserva.describir()
            for reserva in self._reservas
        ]

# 6. SIMULACION DE 12 OPERACIONES

def ejecutar_demo():

    sistema = GestorSoftwareFJ()

    print("\n========== SISTEMA INTEGRAL SOFTWARE FJ ==========")

    # OPERACION 1: Registro correcto de un cliente

    try:

        cliente1 = Cliente(
            "CLI-001",
            "Ana Perez",
            "ana@gmail.com",
            "12345678"
        )

        sistema.registrar_cliente(cliente1)

        print("1. Cliente registrado:", cliente1.describir())

    except (TypeError, ValueError) as error:

        logger.exception("Operacion 1: error registrando cliente")

        print("1. No se pudo registrar el cliente:", error)


    # OPERACION 2: Registro con correo invalido

    try:

        Cliente(
            "CLI-002",
            "Carlos Ruiz",
            "correo-invalido",
            "87654321"
        )

    except (TypeError, ValueError) as error:

        logger.exception("Operacion 2: datos invalidos de cliente")

        print("2. Error esperado al crear cliente:", error)


    # OPERACION 3: Documento con tipo incorrecto

    try:

        Cliente(
            "CLI-003",
            "Laura Diaz",
            "laura@gmail.com",
            12345
        )

    except (TypeError, ValueError) as error:

        logger.exception("Operacion 3: documento invalido")

        print("3. Error esperado en documento:", error)


    # OPERACION 4: Registro de un segundo cliente

    try:

        cliente2 = Cliente(
            "CLI-004",
            "Pedro Gomez",
            "pedro@gmail.com",
            "11223344"
        )

        sistema.registrar_cliente(cliente2)

        print("4. Segundo cliente registrado correctamente.")

    except (TypeError, ValueError) as error:

        logger.exception("Operacion 4: error registrando segundo cliente")

        print("4. Error:", error)


    # OPERACION 5: Creacion correcta de una sala

    try:

        sala = ReservaSala(
            "SER-001",
            "Sala de reuniones",
            50000,
            20
        )

        sistema.registrar_servicio(sala)

        print("5. Servicio creado:", sala.describir())

    except (TypeError, ValueError) as error:

        logger.exception("Operacion 5: error creando sala")

        print("5. Error:", error)


    # OPERACION 6: Creacion de servicio con precio invalido

    try:

        AlquilerEquipo(
            "SER-ERR",
            "Portatil",
            -100,
            5
        )

    except (TypeError, ValueError) as error:

        logger.exception("Operacion 6: servicio invalido")

        print("6. Error esperado al crear servicio:", error)


    # OPERACION 7: Creacion correcta de alquiler de equipos

    try:

        equipos = AlquilerEquipo(
            "SER-002",
            "Alquiler de portatiles",
            30000,
            3
        )

        sistema.registrar_servicio(equipos)

        print("7. Servicio creado:", equipos.describir())

    except (TypeError, ValueError) as error:

        logger.exception("Operacion 7: error creando alquiler")

        print("7. Error:", error)


    # OPERACION 8: Reserva correcta con impuesto y descuento

    try:

        reserva1 = sistema.crear_reserva(
            "RES-001",
            cliente1,
            sala,
            2,
            10,
            impuesto=19,
            descuento=10
        )

        reserva1.procesar()

        print(reserva1.describir())

    except (ErrorSoftwareFJ, TypeError, ValueError) as error:

        logger.exception("Operacion 8: error en reserva correcta")

        print("8. Error:", error)


    # OPERACION 9: Reserva que supera la capacidad de la sala

    try:

        reserva2 = sistema.crear_reserva(
            "RES-002",
            cliente2,
            sala,
            2,
            30
        )

        reserva2.procesar()

    except (ErrorSoftwareFJ, TypeError, ValueError) as error:

        logger.exception("Operacion 9: reserva fallida por capacidad")

        print("9. Reserva fallida controladamente:", error)


    # OPERACION 10: Solicitud de mas equipos de los disponibles

    try:

        reserva3 = sistema.crear_reserva(
            "RES-003",
            cliente1,
            equipos,
            1,
            8
        )

        reserva3.procesar()

    except (ErrorSoftwareFJ, TypeError, ValueError) as error:

        logger.exception("Operacion 10: equipos insuficientes")

        print("10. Reserva fallida controladamente:", error)


    # OPERACION 11: Cancelacion de una reserva confirmada

    try:

        reserva1.cancelar()

        print(
            "11. Reserva RES-001 cancelada. Estado:",
            reserva1.estado
        )

    except (ErrorSoftwareFJ, TypeError, ValueError) as error:

        logger.exception("Operacion 11: error cancelando reserva")

        print("11. Error:", error)


    # OPERACION 12: Intentar cancelar nuevamente la reserva

    try:

        reserva1.cancelar()

    except ReservaNoPermitidaError as error:

        logger.exception("Operacion 12: cancelacion no permitida")

        print("12. Error esperado al cancelar nuevamente:", error)


    # RESUMEN FINAL DE LAS RESERVAS

    print("\n---------- RESUMEN DE RESERVAS ----------")

    for descripcion in sistema.listar_reservas():

        print(descripcion)

    print(
        "\nProceso terminado. Los eventos y errores "
        "se guardaron en el archivo software_fj.log"
    )

    logger.info(
        "Finalizo la simulacion de operaciones del sistema Software FJ"
    )

# 7. EJECUCION PRINCIPAL DEL PROGRAMA

if __name__ == "__main__":
    ejecutar_demo()

# FIN TERCERA PARTE

