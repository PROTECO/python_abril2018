# Escriba un programa de Python que imprima cada elemento y su tipo correspondiente en la siguiente lista.
# Lista de ejemplo : datalist = [1452, 11.23, 1 + 2j, True, 'w3resource', (0, -1), [5, 12], {"clase": 'V', 'section': 'A'} ]
#################################################################################################

datalist = [1452, 11.23, 1 + 2j, True, 'w3resource', (0, -1), [5, 12], {"clase": 'V', 'section': 'A'} ]
for dato in datalist:
	print("Dato: ",dato,"Tipo: ",type(dato))