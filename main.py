import cv2
import numpy as np
'Librerias para utilizar la transformada y manejo de arrays'

imagen = cv2.imread('fotoEjemplo.png')
'Cargo la imagen'
imagenEscalaGris = cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)

'transformo la imagen a escala de grises o binario'

puntos = cv2.Canny(imagenEscalaGris,50,150,apertureSize=3)

'La función encuentra bordes en la imagen de entrada y los marca en los bordes del mapa de salida usando el algoritmo Canny. El valor más pequeño entre umbral1 y umbral2 se utiliza para la vinculación de bordes. El valor más grande se usa para encontrar segmentos iniciales de bordes fuertes.'

lineasDetectadas = cv2.HoughLines(puntos,1,np.pi/180,90)

'Esta funcion encuentra lineas en una imagen binaria usando la transofmrada standard de Hough, recibe la imagen binaria, el rho, el theta y el tamaño maximo del acumulador. cv2.HoughLines(image,rho,theta,threshhold)'

for line in lineasDetectadas:
   rho,theta=line[0]
   a=np.cos(theta)
   b=np.sin(theta)
   x0=a*rho
   y0=b*rho
   'x1 guarda el valor redondeado de r*cos(theta)-1000* sin(theta)'
   x1 = int(x0+1000*(-b))
   'y1 guarda el valor redondeado de r*sin(theta)-1000* cos(theta)'
   y1 = int(y0+1000*(a))
   'x2 guarda el valor redondeado de r*cos(theta)-1000* sin(theta)'
   x2 = int(x0-1000*(-b))
   'y2 guarda el valor redondeado de r*sin(theta)-1000* cos(theta)'
   y2 = int(y0-1000*(a))
   cv2.line(imagen,(x1,y1),(x2,y2),(255,0,255),2)

'Dibuja las lineas sobre la imagen binaria'

cv2.imshow("Lineas", imagen)
'Muesrtro la imagen por pantalla'
cv2.waitKey(0)
'Pulsar para salir'