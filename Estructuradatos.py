print("Estructura de datos")
# Implementación de un árbol binario en Python

class Node:
    def __init__(self, key):
        self.left = None  # Hijo izquierdo
        self.right = None  # Hijo derecho
        self.val = key  # Valor del nodo

class BinaryTree:
    def __init__(self):
        self.root = None  # Raíz del árbol

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)  # Si el árbol está vacío, se inserta la raíz
        else:
            self._insert_rec(self.root, key)  # Inserción recursiva

    def _insert_rec(self, node, key):
        if key < node.val:
            if node.left is None:
                node.left = Node(key)  # Inserta a la izquierda
            else:
                self._insert_rec(node.left, key)  # Continúa a la izquierda
        else:
            if node.right is None:
                node.right = Node(key)  # Inserta a la derecha
            else:
                self._insert_rec(node.right, key)  # Continúa a la derecha

    def inorder(self, node):
        if node:
            self.inorder(node.left)  # Visita el subárbol izquierdo
            print(node.val, end=' ')  # Visita el nodo
            self.inorder(node.right)  # Visita el subárbol derecho