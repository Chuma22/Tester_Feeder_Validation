import configparser
import time
import os

directory = '../StationConfig/'
name_file = 'Parameters.ini'
file = directory + name_file

ruta_archivo_ini = os.path.join(os.path.dirname(__file__), '..', 'StationConfig', 'Parameters.ini')

def readParameters():
    config = configparser.ConfigParser()
    config.read(ruta_archivo_ini)
    return config

def createParameters(config):

    Parameters = {}
    for seccion in config.sections():
        Parameters[seccion] = {}

        for clave in config.options(seccion):  

            if(seccion == "int_InitialValues" or seccion == "int_Indicators" or seccion == "Addresses_D" or seccion == "Factor_Conversion"):
                Parameters[seccion][clave] = int(config.get(seccion, clave))

            elif(seccion == "Addresses_W"):
                Parameters[seccion][clave] = float(config.get(seccion, clave))

            elif(seccion == "Model1" or seccion == "Model2"):
                if (clave == "matrix"):
                    list_1 = config.get(seccion, clave)
                    list_2 = list_1.split(",")
                    list_3 = None
                    list_4 = []
                    for i in range(len(list_2)):
                        list_3 = list_2[i]
                        list_4.append(list_3.split("x"))
                    Parameters[seccion][clave] = list_4

                elif (clave == "x" or clave == "y"):
                    list_1 = config.get(seccion, clave)
                    list_2 = list_1.split(",")
                    Parameters[seccion][clave] = list_2

                elif (clave == "len_xp" or clave == "len_yp"):
                    Parameters[seccion][clave] = config.get(seccion, clave)

                elif (clave == "th"):
                    list_1 = config.get(seccion, clave)
                    Parameters[seccion][clave] = list_1.split(",")

                else:
                    Parameters[seccion][clave] = int(config.get(seccion, clave))
                    
            elif (config.get(seccion, clave) == "TRUE"):
                Parameters[seccion][clave] = True

            elif (config.get(seccion, clave) == "FALSE"):
                Parameters[seccion][clave] = False
            
            else:
                Parameters[seccion][clave] = config.get(seccion, clave)

    return Parameters
 
def getParameters():
  
    config = readParameters()
    Parameters = createParameters(config)
    return Parameters

def saveParameters(Parameters = dict):
    config = configparser.ConfigParser()

    tiempo_actual = time.time()
    estructura_tiempo = time.localtime(tiempo_actual)
    hora_actual = time.strftime("%Y%m%d_%H%M%S", estructura_tiempo)
    file_new = hora_actual + '_' + name_file

    ruta_archivo_nuevo_ini = os.path.join(os.path.dirname(__file__), '..', 'StationConfig', file_new)

    # Agregar los datos del diccionario al objeto ConfigParser
    for seccion, opciones in Parameters.items():
        config.add_section(seccion)
        for clave, valor in opciones.items():
            # print(seccion, clave, valor)
            config.set(seccion, clave, str(valor))

    # Guardar los datos en un archivo INI
    with open(ruta_archivo_nuevo_ini, 'x') as archivo_ini:
        config.write(archivo_ini)

if __name__ == "__main__":

    Parameters = getParameters()
    Parameters["Console_Log"]["console_log"] = "Hello, World!"
    saveParameters(Parameters)
    print(Parameters)
