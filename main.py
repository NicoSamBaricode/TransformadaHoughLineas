import cv2
import numpy as np

imagen = cv2.imread('fotoEjemplo.png')
imagenEscalaGris = cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
puntos = cv2.Canny(imagenEscalaGris,50,150,apertureSize=3)
lineasDetectadas = cv2.HoughLines(puntos,1,np.pi/180,90)

for line in lineasDetectadas:
   rho,theta=line[0]
   a=np.cos(theta)
   b=np.sin(theta)
   x0=a*rho
   y0=b*rho
   x1 = int(x0+1000*(-b))
   y1 = int(y0+1000*(a))
   x2 = int(x0-1000*(-b))
   y2 = int(y0-1000*(a))
   cv2.line(imagen,(x1,y1),(x2,y2),(255,0,255),2)

cv2.imshow("Lineas", imagen)
cv2.waitKey(0)