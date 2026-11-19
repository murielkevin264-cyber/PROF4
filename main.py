


# PROGRAMA PRINCIPAL SOFTWARE FJ

import importlib.util
import sys
from abc import abstractmethod


# Funcion para cargar los archivos
def cargar_archivo(nombre_modulo, nombre_archivo):

    especificacion = importlib.util.spec_from_file_location(
        nombre_modulo, nombre_archivo
    )

    modulo = importlib.util.module_from_spec(especificacion)
    sys.modules[nombre_modulo] = modulo

    return modulo


# PRIMERA PARTE: DAVID

clientes = cargar_archivo(
    "clientes",
    "DavidAchicanoy-ClassAbstracta-ClassCliente.py"
)

especificacion = clientes.__spec__
especificacion.loader.exec_module(clientes)

EntidadGeneral = clientes.EntidadGeneral
Cliente = clientes.Cliente


# SEGUNDA PARTE: KEVIN

servicios = cargar_archivo(
    "servicios",
    "Aporte_kevin_Muriel.py"
)

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
)

reservas.EntidadGeneral = EntidadGeneral
reservas.Cliente = Cliente
reservas.Servicio = Servicio
reservas.ReservaSala = ReservaSala
reservas.AlquilerEquipo = AlquilerEquipo
reservas.AsesoriaEspecializada = AsesoriaEspecializada

reservas.__spec__.loader.exec_module(reservas)


# EJECUCION DEL PROGRAMA

if __name__ == "__main__":
    reservas.ejecutar_demo()

    