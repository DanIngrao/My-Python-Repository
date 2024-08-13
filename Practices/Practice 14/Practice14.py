import cv2
import face_recognition as fr
import numpy as np

# Cargar imagenes
foto_control = cv2.imread('Practices\\Practice 14\\FotoA.jpg')
foto_prueba = cv2.imread('Practices\\Practice 14\\FotoB.jpg')

# Mostrar imagenes
cv2.imshow('Foto Control', foto_control)
cv2.imshow('Foto Prueba', foto_prueba)

# Pasar imagenes a RGB
foto_control = cv2.cvtColor(foto_control, cv2.COLOR_BGR2RGB)
foto_prueba = cv2.cvtColor(foto_prueba, cv2.COLOR_BGR2RGB)

# Localizar cara control
cara_control = fr.face_locations(foto_control)

# Mantener programa abierto
cv2.waitKey(0)