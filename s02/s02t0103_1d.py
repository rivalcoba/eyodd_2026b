# Eliminacion
# Importando funcion Array
# del modulo array y renombrando
# como arr
from array import array as arr

# Importando una funcion de otro
# Archivo
from s02t0102_1d import print_array

my_array = arr('i',[2,10,15,20,10])

print("--- ANTES DE LA ELIMINACION ---")
print_array(my_array)

# Eliminación
try:
 my_array.remove(100)
except:
 print(f"no se encuentra en el arreglo")
print("--- DESPUES DE LA ELIMINACION ---")
print_array(my_array)



