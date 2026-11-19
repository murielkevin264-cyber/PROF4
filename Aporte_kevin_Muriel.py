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