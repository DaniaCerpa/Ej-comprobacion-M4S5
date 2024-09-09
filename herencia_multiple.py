class A:
    def __init__(self):
        print ("Pertenezco a la clase A")
        
    def metodo_a(self):
        print("Método heredado de A")
        
class B:
    def __init__(self):
        print ("Clase B")
        
    def metodo_b(self):
        print("Método heredado de B")
        
#Creación de clase C con herencia multiple de las clases B y A en este orden.
class C(B,A):
    def metodo_c(self):
        print("Método de clase C")
        
#Creación de instancia de clase C (imprimira el metodo constructor de la clase B, por orden en la herencia multiple especificada)
a = C()

#Ejecución de metodos para la nueva instancia.
a.metodo_a()
a.metodo_b()
a.metodo_c()