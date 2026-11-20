


# PROGRAMA PRINCIPAL SOFTWARE FJ

import importlib.util # se crea un modulo para importar archivos de manera dinamica
import sys
from abc import abstractmethod  # se importa la clase abstracta para poder usarla en los modulos importados


# Funcion para cargar los archivos
def cargar_archivo(nombre_modulo, nombre_archivo):

    especificacion = importlib.util.spec_from_file_location( 
        nombre_modulo, nombre_archivo
    )  # se crea una especificacion del modulo a importar

    modulo = importlib.util.module_from_spec(especificacion) # se crea un modulo a partir de la especificacion
    sys.modules[nombre_modulo] = modulo

    return modulo # se retorna el modulo importado


# PRIMERA PARTE: DAVID

clientes = cargar_archivo(
    "clientes",
    "DavidAchicanoy-ClassAbstracta-ClassCliente.py"
)    # se carga el archivo de clientes

especificacion = clientes.__spec__
especificacion.loader.exec_module(clientes) # se ejecuta el modulo de clientes

EntidadGeneral = clientes.EntidadGeneral
Cliente = clientes.Cliente


# SEGUNDA PARTE: KEVIN

servicios = cargar_archivo(
    "servicios",
    "Aporte_kevin_Muriel.py"
)    # se carga el archivo de servicios

servicios.EntidadGeneral = EntidadGeneral
servicios.abstractmethod = abstractmethod

servicios.__spec__.loader.exec_module(servicios)

Servicio = servicios.Servicio
ReservaSala = servicios.ReservaSala
AlquilerEquipo = servicios.AlquilerEquipo
AsesoriaEspecializada = servicios.AsesoriaEspecializada


# TERCERA PARTE: LAURA

reservas = cargar_archivo(
    "reservas",
    "Aporte-LauraRamos.py"
) # se carga el archivo de reservas

reservas.EntidadGeneral = EntidadGeneral
reservas.Cliente = Cliente
reservas.Servicio = Servicio
reservas.ReservaSala = ReservaSala
reservas.AlquilerEquipo = AlquilerEquipo
reservas.AsesoriaEspecializada = AsesoriaEspecializada

reservas.__spec__.loader.exec_module(reservas) # se ejecuta el modulo de reservas


# EJECUCION DEL PROGRAMA

if __name__ == "__main__": # se ejecuta el programa principal
    reservas.ejecutar_demo() # se ejecuta la funcion de demo del modulo de reservas

    