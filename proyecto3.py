# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 08:56:55 2023

@author: hecto
"""

#proyecto #3
#Hétorio
#TecNM, Ags
#Posgrado en C. Ambientales
#Control de la contaminación atmosferica
#07/03/2023

#Determinacion de gradiente potecial de temperatura a partir
#de dos condiciones de temperatura a dos diferentes niveles del
#suelo

#damos de alta los datos
T = [24, 18]    #°F o °C
z = [0, 600]   #ft o m

#Definir unidades del problema (n = 0, ingles. n = 1 internacional)
n = 1

#gradiente de temperatura adiabatico
gamma = [-0.0054, -0.0098]

#definimos la función del gradiente de temperatura
#potencial
def theta_z(T,z,gamma):
    theta = (T[0] - T[1])/(z[0] - z[1]) - gamma
    return theta

#evaluamos nuestra función
theta = theta_z(T,z,gamma[n])

#vamos a usar if para presentar la estabilidad
#de nuestro sistema
if theta < 0:
    print('El sistema es INESTABLE')
if theta == 0:
    print('El sistema es ESTABLE')
if theta > 0:
    print('El sistema es FUERTEMENTE ESTABLE')

if n == 0:
    print('El valor del gradiente potencial de temperatura es: ' + str(theta*1000) + '°F/1000ft')
else:
    print('El valor del gradiente potencial de temperatura es: ' + str(theta*100) + '°C/100m')