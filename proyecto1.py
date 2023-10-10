# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 08:41:30 2023

@author: hectorio xd
"""

#Proyecto para deteminar la estabilidad atmosferica a partir del
#gradiente de temperatura adiabatico y atmosferico (real)

#importamos librerias
import matplotlib.pyplot as plt

#parametros
To = 25     #°F ó °C
zo = 0      #ft ó m (esta no se modifica para este ejercicio)
T = 5      #°F ó °C
z = 2000    #ft ó m

#definimos unidades del cáluclo
#si n = 0 SI
#si n = 1 sistema ingles
n = 0

##################################################################

#gradiente de temperaturas (ingles o SI)
gamma = [[-0.0098, -0.0054]]

#seleccionar el valor de gamma
gamma = gamma[0][n]

#evaluamos el gradiente temperatura
dT = -(T-To)/(z-zo)

#determinamos la estabilidad
if dT < gamma:
    estabilidad = 'Estable'
if dT == gamma:
    estabilidad = 'Neutro'
if dT > gamma:
    estabilidad = 'Inestable'

#determinar las ordenas al origen
#para el gradiente ambiental
b = To + zo*dT

#el gradiente adiabatico
ba = To - zo*gamma

#damos de alta variables donde se  guardaran
#las temperaturas
T_amb = []
T_adi = []
altura = []

#determinar los valores para graficar
for i in range(2):
    T_amb.append(-zo*dT + b)
    T_adi.append(zo*gamma + ba)
    altura.append(zo)
    zo = z*1

#diccionario
unid_T = {0:'°C',1:'°F'}
unid_alt = {0:'m',1:'ft'}

#grafica
plt.plot(T_amb, altura, T_adi, altura)
plt.legend(['Gradiente ambiental', 'Gradiente adiabático'])
plt.xlabel('Temperatura ' + '(' + unid_T[n] + ')')
plt.ylabel('Altura ' + '(' + unid_alt[n] + ')')
plt.title('La estabilidad atmosferica es: ' + estabilidad)





