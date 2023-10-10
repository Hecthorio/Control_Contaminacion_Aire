# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 08:51:17 2023

@author: hecto
"""
#TecNM/Ags
#Posgrado en C. Ambientales
#Hectorio...

#proyecto 2
#script para determinar la temperatura potencial a partir
#de la presion y la temperatura

#Datos de entrada para el codigo
T_F = [70, 70, 60]     #°F
P_F = [970, 925, 935]  #mbar
T_C = [25, 30, 25]     #°C
P_C = [820, 950, 930]  #mbar

#declarar la funcion temperatura potencial
def theta(T,P):
    theta = T*(1000/P)**0.288
    return theta

#función para covertir a T ambsoluta
def T_to_K(T_C):
    T = T_C + 273.15
    return T

def T_to_R(T_F):
    T = T_F + 459.6
    return T

#convertir las T a T absolutas
for i in range(len(T_F)):
    T_F[i] = T_to_R(T_F[i])
    T_C[i] = T_to_K(T_C[i])

#damos de alta las variables donde guardamos la información
#del gradiente potencial para T en R y K
theta_1 = []
theta_2 = []

#determinar las temperaturas potenciales
for i in range(len(T_F)):
    theta_1.append(theta(T_F[i], P_F[i]))     #theta_1 evalua las T en R
    theta_2.append(theta(T_C[i], P_C[i]))     #theta_2 evalua las T en K