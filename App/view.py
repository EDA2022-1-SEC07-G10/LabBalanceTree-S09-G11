"""
 * Copyright 2020, Departamento de sistemas y Computación
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

import sys
import config
from App import controller
assert config

"""
La vista se encarga de la interacción con el usuario.
Presenta el menu de opciones  y  por cada seleccion
hace la solicitud al controlador para ejecutar la
operación seleccionada.
"""

# ___________________________________________________
#  Ruta a los archivos
# ___________________________________________________


crimefile = "Boston Crimes//crime-utf8.csv"
cont = None
# ___________________________________________________
#  Menu principal
# ___________________________________________________


def printMenu():
    print("\n")
    print("*******************************************")
    print("Bienvenido")
    print("1- Inicializar Analizador")
    print("2- Cargar información de crimenes")
    print("3- Consultar crimenes en un rango de fechas")
    print("4- Consultar crimenes por codigo y fecha")
    print("5- Consultar crimenes por un rango de areas")
    print("0- Salir")
    print("*******************************************")


"""
Menu principal
"""
while True:
    printMenu()
    inputs = input("Seleccione una opción para continuar\n>")

    if int(inputs[0]) == 1:
        print("\nInicializando....")
        # cont es el controlador que se usará de acá en adelante
        cont = controller.init()

    elif int(inputs[0]) == 2:
        print("\nCargando información de crimenes ....")
        controller.loadData(cont, crimefile)
        print("Crimenes cargados: " + str(controller.crimesSize(cont)))
        print("Altura del arbol: " + str(controller.indexHeight(cont)))
        print("Elementos en el arbol: " + str(controller.indexSize(cont)))
        print("Menor Llave: " + str(controller.minKey(cont)))
        print("Mayor Llave: " + str(controller.maxKey(cont)))

        print("Altura del arbol de areas: " + str(controller.indexHeightAreas(cont)))
        print("Elementos en el arbol de areas: " + str(controller.indexSizeAreas(cont)))
        print("Menor Llave de areas: "+str(controller.minKeyAreas(cont)))
        print("Mayor Llave de areas: "+str(controller.maxKeyAreas(cont)))
    elif int(inputs[0]) == 3:
        print("\nBuscando crimenes en un rango de fechas: ")
        initialDate = input("Fecha Inicial (YYYY-MM-DD): ")
        finalDate = input("Fecha Final (YYYY-MM-DD): ")
        total = controller.getCrimesByRange(cont, initialDate, finalDate)
        print("\nTotal de crimenes en el rango de fechas: " + str(total))

    elif int(inputs[0]) == 4:
        print("\nBuscando crimenes x grupo de ofensa en una fecha: ")
        initialDate = input("Fecha (YYYY-MM-DD): ")
        offensecode = input("Ofensa: ")
        numoffenses = controller.getCrimesByRangeCode(cont, initialDate,
                                                      offensecode)
        print("\nTotal de ofensas tipo: " + offensecode + " en esa fecha:  " +
              str(numoffenses))

    elif (int(inputs[0]) == 5):
       
        print("\nBuscando crimenes en un rango de areas: ")
        print("Las areas estan numeradas con enteros (1 - 962)")
        print("Un area desconocida tiene el el numero 9999")
        initialArea = input("Area Inicial: ")
        finalArea = input("Area Final: ")
        numoffenses = controller.getCrimesByRangeArea(cont, initialArea,
                                                        finalArea)
        print("\nTotal de crimenes en el rango de areas: " + str(numoffenses))

    else:
        sys.exit(0)
sys.exit(0)
