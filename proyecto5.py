# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 09:26:54 2023

@author: hecto
"""

#Proyecto 5
#TecNM/ITA
#Posgrado en C en Ambientales
#Control de la contaminación atmosferica

#importar librerias
import numpy as np
import matplotlib.pyplot as plt

#Scritp para determinar la altura de la mezcla
#a partir del gradiente de temperaturas ambiental
#y adiabatico a difentes alturas

#Datos de entrada:
#para el gradiente ambiental
zo = 0      #ft o m
To = 70     #°F o °C
z1 = 2000    #ft o m
T1 = 65     #°F o °C
n = 0       #inglés ó internacional [0,1] 

#para el gradiente adibatico
za = 0      #ft
Tmax = 84   #°F

#Gradiente adiabatico de temperatura
gamma = [-0.0054, -0.0098]   #°F/ft y °C/m

#determinar el gradiente ambiental
dT = (T1-To)/(z1-zo)

#determinar las ordenadas al origen
bamb = zo - To/dT
badi = za - Tmax/gamma[n]

#generar una función para determinar el gradiente de T
def altura(bamb,badi,gamma,n,Tamb,Tadi,dT):
    zamb = bamb + Tamb/dT
    zadi = badi + Tadi/gamma[n]
    return zamb, zadi

#vector de temperaturas
Tamb = np.arange(0,max(To,T1),1)
Tadi = np.arange(0,Tmax)

#determinar las alturas a las diferentes 
#temperaturas
zamb, zadi = altura(bamb,badi,gamma,n,Tamb,Tadi,dT)

#evaluar la altura de mezclado
aam = (bamb*dT-badi*gamma[n])/(dT-gamma[n])

#evaluar en ese pto, cual es la T...
Taam = dT*(aam - bamb)

#diccionario
ejes = {0:['°F','ft'],
        1:['°C','m']}

#vamos a graficar los gradientes de T
plt.plot(Tamb,zamb,'-',Tadi,zadi,'--')
plt.plot(Taam,aam,'o', markerfacecolor ='none')
plt.xlabel('Temperatura ' + ejes[n][0])
plt.ylabel('Altura ' + ejes[n][1])
plt.legend(['Gradiente ambiental',
           'Gradiente adiabático',
           'Altura de mezcla'])
plt.title('La altura de la mezcla es: ' + 
          str(round(aam,2)) + ' ' + ejes[n][1])