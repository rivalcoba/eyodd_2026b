# Importando clase Node
from s02t0201_linked_list import Node

# Creando la clase de una lista enlazada
class SinglyLinkedList:
  # Constructor
  def __init__(self):
    self.head = None
    self.tail = None
    self.size = 0
  
  # Metodo de inserción de Nodo en la lista
  def append(self, data):
    # Creo el nodo
    new_node = Node(data)

    # Si hay un Tail, el nuevo nodo
    # Pasa a ser el nuevo Tail
    if self.tail:
      self.tail.next = new_node
      self.tail = new_node
    # Si no hay tail
    else:
      self.tail = new_node
      self.head = new_node
    # Se incrementa size en 1
    self.size += 1

  # Insertando en posicion intermedia
  # [A->B->C] 0 4
  # [1  2  3]
  # size= 3
  def append_at_location(self, data, index):
    if index < 1 or index > self.size + 1:
      raise IndexError(f"Indice {index} fuera de rango")

    # Crear un nuevo nodo
    new_node = Node(data)

    # Insertar al inicio de la lista
    if index == 1:
      new_node.next = self.head
      self.head = new_node
      if self.tail == None:
        self.tail = new_node
      # Incremento en 1 el tamaño
      self.size += 1
    
    # Creando variables de control
    # para las inserciones intermedias
    current = self.head
    prev = None
    position = 1

    # Traversal (Recorrido)
    while current is not None and position < index:
      prev = current
      current = current.next
      position += 1
    
    # Llegando a la posicion
    # Estoy al final?
    if current is None:
      prev.next = new_node
      self.tail = new_node
      self.size += 1
      return

    # Si llegamos a una posicion intermedia
    # 🚧 TODO: Pendiente de termianar 🚧


# 1 Creo funcion principal
def main():
  # Creando una instancia de una lista enlaza
  my_list = SinglyLinkedList()
  # Agregando elementos a la lista
  my_list.append(30)
  my_list.append(59)
  my_list.append(80)
  my_list.append(100)

  # Recorrer la lista
  for value in my_list.head.iter():
    print(f"{value},", end=" ")
  print()

# Evaluo el valor de __name__
if __name__ == "__main__":
  main()