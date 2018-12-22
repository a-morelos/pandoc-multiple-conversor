#Script para convertir archivos múltiples con pandoc
#@autor: Alberto Morelos
#Fecha: 14 de octubre de 2018
#Versión: 0.1

import argparse, sys, subprocess, io

from shlex import split

parser = argparse.ArgumentParser(description = "Conversor de archivos múltiples mediante pandoc")
parser.add_argument("i", help="extension a buscar, ej. doc")
parser.add_argument("-o", help="formato de salida, ej. html", default="html")

argumentos = parser.parse_args()
ext_entrada = argumentos.i
ext_salida = argumentos.o

#funcion que usa pandoc para convertir el archivo
def ejecutarPandoc(archivo, ext_entrada, ext_salida):
	archivo_salida = archivo.split(".")
	pandoc_parametros = split("pandoc -f {} -t {} -o {} {}".format(ext_entrada, ext_salida, archivo_salida[0] + "." + ext_salida, archivo))
	pandoc_command = subprocess.run(pandoc_parametros)

bash_filter = split("egrep '*.{}$'".format(ext_entrada))

#Ejecuta el equivalente a $ ls | egrep ''
ls = subprocess.Popen(["ls"], stdout=subprocess.PIPE, text=True)
search = subprocess.Popen(bash_filter,stdin=ls.stdout, stdout=subprocess.PIPE)

if(ext_entrada == "md"):
	ext_entrada = "markdown"

for archivo in io.TextIOWrapper(search.stdout):
	ejecutarPandoc(archivo, ext_entrada, ext_salida)
	
print("Conversion terminada con exito")

sys.exit()
	