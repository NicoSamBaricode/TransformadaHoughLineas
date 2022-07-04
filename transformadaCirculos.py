import cv2
import numpy as np

imagen = cv2.imread('fotocirculo.png',0)
imagen = cv2.medianBlur(imagen,5)
ImagenBinaria = cv2.cvtColor(imagen,cv2.COLOR_GRAY2BGR)
# hasta aca carga la imagen y primero la pre procesa y luego la transforma a escala de grises o binaria.

circulos = cv2.HoughCircles(imagen,cv2.HOUGH_GRADIENT,1,20,
                            param1=20,param2=30,minRadius=0,maxRadius=20)
# aplica la transformada de hough utilizando el gradiente, esto evita uilizar un espacio 3d y asi es mas eficiente.
circulos = np.uint16(np.around(circulos))
for i in circulos[0,:]:
    # dibuja el circulo
    cv2.circle(ImagenBinaria,(i[0],i[1]),i[2],(0,255,0),2)
    # dibuja el centro del circulo
    cv2.circle(ImagenBinaria,(i[0],i[1]),2,(0,0,255),3)

cv2.imshow('circulos detectados',ImagenBinaria)

cv2.waitKey(0)
cv2.destroyAllWindows()