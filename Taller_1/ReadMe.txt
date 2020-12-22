AUTORES:

Mateo Aguilar cardona   - maaguilarca@unal.edu.co
Rorigo Alexander Fagua Arevalo   - rafaguaa@unal.edu.co
Alci Rene Ramirez Soto   - alrramirezso@unal.edu.co



ASIGNATURA:

Sistemas Inteligentes 



Este programa se ejecuta en sistema operativo windows

Requerimientos:
1.Tener instalado correctamente python (version 3)
2.Tener habilitado correctamente open Cv (preferiblemente la version 2)
3.Tener instalado correctamente python tesseract
4.Verificar los paths de python y tesseract

En caso de no contar con los requerimientos siga los pasos del tutorial de instalacion(este puede contener
 enlaces externos)


Tutoriales de instalacion 

instalar python y el gestor de paquetes pip

http://lingwars.github.io/blog/instalar-python-en-windows-7.html (si usa windows 7)

si utiliza un windows superior puede descargar las vesiones aqui:(para 32 y 64 bits)

https://www.python.org/downloads/windows/


Instalar pytesseract 
Ir al link:
https://github.com/UB-Mannheim/tesseract/wiki (buscar la version mas conviente 32 o 64 bits)
buscar el apartado de windows

Ejecutar los scripts de pip en caso que falle el programa por alguna importacion

pip3 install --user pip3 install opencv-contrib-python
pip3 install --user pytesseract
pip3 install --user pyautogui
pip3 install --user numpy

EJECUCION DEL PROGRAMA:

Para Ejecutar el programa de ir al pagina de sudokus https://www.epasatiempos.es/sudokus.php y ejecutar 
el programa "main.py" de forma que se visible el sudoku en la pantalla.

Este le mostrara el tablero con los datos tomados mediante una captura de pantalla
y luego se ejecutara el programa que resuleve el sudoku mediante el analisis de numeros, verificando 
que no se repitan en cada fila o columna y luego revisa si no se repite en la caja de 3x3.


CONSIDERACIONES:
El programa fue probado en una pantalla de resolucion 1366x768, como el programa ejecuta un analisis de pixeles
exacto al tomar la captura de pantalla podria generar problemas de lectura si no se cuenta con la misma 
resolucion.

SOLUCION DE PROBLEMAS DE EJECUCION:

1.Para solucionar este problema debera hacer un recorte lo mas preciso posible del sudoku y ver la cantidad de 
pixeles que genera ese recorte. ( se recomienda la aplicacion recortes de windows)

2.Luego cambiarle el tamaño a la imagen anexa al trabajo "selector2.png" y colocarle
las dimensiones encontradas. (si edita la imagen selector.png debera hacer un pasos extra anexo al final 
del documento).

3.Posteriormente en el archivo "tablero.py" debera cambiar los valores 523 de las variables stepy y stepx en las
lineas 10 y 11 por los valores de los pixeles anteriormente encontrados.

Luego de estos pasos el programa debe ejecutarse correctamente.


*************Paso extra*************
Paso extra al editar la imagen selector.png 
Este paso es necesario y obligatorio si cambio la imagen selector.png y no la imagen selector2.png

Debera editar el archivo "pantallazo.py" quitandole el 2 a la linea 10 y continuar desde el paso 3


