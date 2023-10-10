# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 08:34:09 2023

@author: hecto
"""

#TecNM/Aguascalientes
#M en C Ambientales
#Control contaminación atmosferica
#Proyecto 6
#Héctorio

#Script para determinar altura, temperatura potencial
#y gradiente ambiental de temperaturas a partir de
#condiciones de P y T

#liberia
import numpy as np
import matplotlib.pyplot as plt

#Datos:
#Punto de referencia
To = 11     #°C
Po = 1023   #mbar
zo = 30      #m

#A otra altura
T1 = np.array([9.8, 12, 14, 15, 13, 13, 12.6, 1.6, 0.8])    #°C
P1 = np.array([1012, 1000, 998, 969, 906, 878, 850, 725, 700])    #mbar

#Gradiente adiabatico de temperaturas
gamma = [-0.0098, -0.0054]  #°C/m ó °F/ft

#Función para determinar la temperatura potencial
def theta(T,P):
    theta = (T+273.15)*(1000/P)**(0.288)
    return theta

#Evaluar la altura a las condiciones dadas
z1 = zo - (theta(T1,P1) - theta(To,Po) - T1 + To)/gamma[0]

#Determinar el gradiente de T ambiental
dT = (T1-To)/(z1-zo)

#Graficar altura contra temperatura
plt.plot(T1,z1,'o')
plt.plot(To,zo,'o')