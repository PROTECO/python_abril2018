###############################
## Serialización con pickle  ##
###############################

# Serialización de objetos:
# Convertir objetos a cadenas de bytes y viceversa
# Nos permite mantener objetos entre ejecuciones de un script
# No usamos eval o exec para que no nos hackeen y borren todo alv >:v

import pickle
# pickle permite serializar un objeto

#Serializar

D = {'Julio':8,'Ana':9,'Jose':9,'Luis':8,'Jorge':9,'Pedro':10,'Mariana':10}
F = open('datos.pkl','wb') # wb -> write bytes 

pickle.dump(D,F) # pickle.dump(objeto, flujo)
F.close()


#Recrear objeto

f = open('datos.pkl','rb')
calificaciones = pickle.load(f) # pickle.load(flujo)
print(calificaciones)
f.close()

