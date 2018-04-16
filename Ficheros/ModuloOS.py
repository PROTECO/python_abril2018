###########
#Modulo OS#
###########

"""
El modulo Os nos provee de métodos 
parea trabajar de forma portable con las
funcionalidades del sistema Operativo
"""

import os
#Nombre del sistema Operativo
#print("Nombre del SO: ",os.name)

#os.system("ls")#Para linux ls

#print("La carpeta actual es:",os.listdir(".."))
#para Mac /Users/nombreusuario
"""
directorios=os.listdir('C:\\')#para Linux/
i=0
for directorio in directorios:
	print("Directorio %i: %s"%(i,directorio))
	i+=1
"""
os.mkdir("NuevacarpetaPython2")
print(os.listdir("."))

os.rmdir("NuevacarpetaPython")
print(os.listdir("."))