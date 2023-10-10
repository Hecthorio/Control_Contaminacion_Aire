# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 08:30:54 2023

@author: hecto
"""

#Proyecto 4
#TecNM/ITA
#M en C Ambientales
#Control de la contaminación
#Héctor Olmos
#determinación de perfil de velocidades a partir de la ley
#de pontencia de Deacon

#librerias
import matplotlib.pyplot as plt
import numpy as np

#Datos de entrada al modelo (independiente de las unidades)
u1 = 2     #mi/h o (pueden ser las unidades que sean)
z1 = 10     #m
z2 = 200    #m
n = 1       #el valor de n esta definido por la estabilidad

#condiciones de estabilidad
con_estab = {0:['Tasa de cambio grande',0.2],
             1:['Tasa de cambio pequeña o cero',0.25],
             2:['Inversión moderada',0.33],
             3:['Inversión grande',0.5]}

#definir la función de ley potencias de Deacon
def vel(u1, z, z1, n):
    u = u1*(z/z1)**(n/(2-n))
    return u

#determinar el valor de la velocidad
u2 = vel(u1, z2, z1, con_estab[n][1])

#definir el vector de alturas
z = np.arange(0,620,20)

#evaluar las velocidades para todas las alturas
u = vel(u1, z, z1, con_estab[n][1])

#graficar perfil de velocidades
plt.plot(u,z)
plt.plot(u2,z2,'o')
plt.xlabel('Velocidad (m/s)')
plt.ylabel('Altura (m)')
plt.title('Perfil de velocidades de Deacon para: ' + con_estab[n][0])
plt.legend(['Perfil de velocidades 0-600 m', 'velocidad a ' + 
            str(z2) + 'm es: ' + str(round(u2,1)) + 'm/s'])
plt.grid(visible = True)