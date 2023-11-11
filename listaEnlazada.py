# Clase  Libro que represeta un libro de la biblioteca 
class Libro:
    # método constructor que se ejecua cuando se crea un objeto de la clase
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn

# Clase Nodo que rpresenta un elemento que se puede agregar, eliminar o revisar de la biblioteca
# se puede entender como el lugar que tiene el libro en la biblioteca (ESPACIO) 
class Nodo:
    # Método constructor de la clase que se ejecuta cada vez que se crea un objeto de tipo NODO
    # nodo tiene dos atributos (variables), la referencia a si mismo y un objeto de tipo libro
    def __init__(self, libro):
        self.libro = libro
        self.siguiente = None

#Clase que representa la biblioteca, es decir, que tiene una lista de los libros 
class Biblioteca:
    #Método constructor qque 
    def __init__(self):
        # variable de la clase que se inicializa como NULA
        self.inicio = None

    # Método que valora si inicio es NULO o no.  Se pregunta "is None"
    def esta_vacia(self):
        return self.inicio is None
    
    # Método que agrega un libro en forma consecutiva, detrás del último de la lista
    # recibe la referencia a si mismo (self) y un objeto libro que va agregar
    def agregar_libro(self, libro):
        
        # crea objeto de tipo NODO
        nuevo_nodo = Nodo(libro)
        # si esta vacia convierte el nodo vacio en el nuevo nodo
        if self.esta_vacia():
            self.inicio = nuevo_nodo
        # Por falso va agregar el nodo al final de la lista
        else:
            # ubica el inicio de la lista 
            actual = self.inicio
            # Recorre la lista hasta llegar al último nodo y agrega el nuevo 
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    # Agrega el nodo al comienzo de la lista
    def agregar_libro_al_comienzo(self, libro):
        nuevo_nodo = Nodo(libro)
        nuevo_nodo.siguiente = self.inicio
        # cambia el nodo inicio respecto al siguiente
        self.inicio = nuevo_nodo

    def agregar_libro_entre_nodos(self, libro, nodo_anterior, nodo_siguiente):
        nuevo_nodo = Nodo(libro)
        nodo_anterior.siguiente = nuevo_nodo
        nuevo_nodo.siguiente = nodo_siguiente

    def mostrar_libros(self):
        actual = self.inicio
        while actual:
            libro = actual.libro
            print(f'Título: {libro.titulo}, Autor: {libro.autor}, ISBN: {libro.isbn}')
            actual = actual.siguiente

# Ejemplo de uso
if __name__ == "__main__":
    biblioteca = Biblioteca()
    
    libro1 = Libro("El Señor de los Anillos", "J.R.R. Tolkien", "978-84-450-7378-6")
    libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", "978-84-376-0494-7")
    libro3 = Libro("1984", "George Orwell", "978-84-9759-020-1")
    
    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)
    biblioteca.agregar_libro(libro3)

    print("Biblioteca:")
    biblioteca.mostrar_libros()

    # Agregar un libro al comienzo de la lista
    libro_nuevo = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", "978-84-376-0494-7")
    biblioteca.agregar_libro_al_comienzo(libro_nuevo)

    print("\nBiblioteca después de agregar un libro al comienzo:")
    biblioteca.mostrar_libros()

    # Agregar un libro entre dos nodos indicados previamente
    libro_intermedio = Libro("Rayuela", "Julio Cortázar", "978-84-376-0494-7")
    nodo_anterior = biblioteca.inicio  # Nodo del libro "El Señor de los Anillos"
    nodo_siguiente = nodo_anterior.siguiente  # Nodo del libro "Cien años de soledad"
    biblioteca.agregar_libro_entre_nodos(libro_intermedio, nodo_anterior, nodo_siguiente)

    print("\nBiblioteca después de agregar un libro entre dos nodos:")
    biblioteca.mostrar_libros()