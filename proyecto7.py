# -*- coding: utf-8 -*-
"""
Created on Tue May 16 08:36:18 2023

@author: hecto
"""

#ITA
#M. en C. Ing Ambiental
#Control contaminación atmosferica

#Script para evaluar el modelo de emisión guassiana,
#a partir de condiciones de estabilidad y parametros
#atmosfericos.

#Libreria
import numpy as np
import matplotlib.pyplot as plt

##########################################################
#            DAR DE ALTA LAS VARIABLES                   #
##########################################################

#NOTA: si y=0 y z=0 se evalua la concentración 
#sobre la linea central

Q = 160             #tasa de emisión, g/s
H = 60              #altura efectiva, m (H = h + dh)
u = 6               #velocidad, m/s
estabilidad = "D"   #Estabilidad atmosferica (A-F)
x = 500             #distancia en x (m)
y = 50              #distancia en y (m)
z = 0               #distancia en z (m)
Vs = 3              #velocidad de salida de los gases (m/s)
T = 300             #temperatura de la atmosfera (K)
Ts = 400            #temperatura a la que salen los gases (K)

##########################################################
#         EVALUAR LOS VALORES DE SIGMA (zy)              #
##########################################################

#damos de alta los diccionarios con la información de las
#constantes del modelo

a = {"A":213,
     "B":156,
     "C":104,
     "D":68,
     "E":50.5,
     "F":34}

#cdf_L se utiliza cuando x < 1 km
cdf_L = {"A" : [440.8, 1.941, 9.27],
         "B" : [106.6, 1.149, 3.3],
         "C" : [61, 0.911, 0],
         "D" : [33.2, 0.725, -1.7],
         "E" : [22.8, 0.678, -1.3],
         "F" : [14.35, 0.74, -0.35]}

#cdf_H se utiliza cuando x > 1 km
cdf_H = {"A" : [459.7, 2.094, -9.6],
         "B" : [108.2, 1.098, 2],
         "C" : [61, 0.911, 0],
         "D" : [44.5, 0.516, -13],
         "E" : [55.4, 0.305, -34],
         "F" : [62.6, 0.18, -48.6]}

#este parametro es cte para todas la estabilidades
b = 0.894

#damos de alta las funciones
#NOTA: x se transforma de m a km en la función

#función para determinar sigma-y
def sigma_y(a,b,x,estabilidad):
    sigmay = a[estabilidad]*(x/1000)**b
    return sigmay

#función para determinar sigma-z
def sigma_z(cdf_H, cdf_L, x, estabilidad):
    if x < 1000:
        sigmaz = cdf_L[estabilidad][0]*(x/1000)**cdf_L[estabilidad][1] + cdf_L[estabilidad][2]
    if x >= 1000:
        sigmaz = cdf_H[estabilidad][0]*(x/1000)**cdf_H[estabilidad][1] + cdf_H[estabilidad][2]
    return sigmaz

#Damos de alta la función de concentración
def con(Q,u,sigmay,sigmaz,y,z,H):
    C = Q/(2*np.pi*u*sigmay*sigmaz)*np.exp(-y**2/(2*sigmay**2))*\
    (np.exp((-(z-H)**2)/(2*sigmaz**2)) + np.exp((-(z+H)**2)/(2*sigmaz**2)))
    return C

#def altura()

#evaluar el valor de C a las condiciones dadas
#evalumos 1ro las sigmas
sigmay = sigma_y(a, b, x, estabilidad)
sigmaz = sigma_z(cdf_H, cdf_L, x, estabilidad)

#ahora si, evaluamos la concentración (ug/m3)
C = con(Q, u, sigmay, sigmaz, y, z, H)/1e-6

# #declaramos las listas donde se guardara la información
C = []
X = []
xf = 10000  #ditancia en metros
x = 500     #distancia en metros

n = 1000    #contador de seguridad

# #generamos un ciclo
while x <= xf:
     sigmay = sigma_y(a, b, x, estabilidad)
     sigmaz = sigma_z(cdf_H, cdf_L, x, estabilidad)
     c = con(Q, u, sigmay, sigmaz, y, z, H)/1e-6
     C.append(c)
     X.append(x)
     x = x + 100
     #esta sección del codigo es por seguridad
     if len(C) >= n:
         print('Tu codigo se ciclo')
         break

#evaluación de la c_max y la distancia de donde ocurre
#ese máximo

# sigma_z = 0.707*H

# x_menor = ((sigma_z - cdf_L[estabilidad][2])/cdf_L[estabilidad][0])**(1/cdf_L[estabilidad][1])*1000
# x_mayor = ((sigma_z - cdf_H[estabilidad][2])/cdf_H[estabilidad][0])**(1/cdf_H[estabilidad][1])*1000

# C_max_menor = (0.117*Q/(u*sigma_z*sigma_y(a, b, x_menor, estabilidad)))/1e-6
# C_max_mayor = (0.117*Q/(u*sigma_z*sigma_y(a, b, x_mayor, estabilidad)))/1e-6

#graficar nuestra información
plt.plot(X,C)
plt.xlabel('x, distancia (m)')
plt.ylabel('Concentración contaminante ($\mu$g/$m^3$)')
plt.title('Perfil de concentraciones a nivel suelo')