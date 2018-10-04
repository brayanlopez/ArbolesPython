class Nodo:
    def __init__(self, value):
        self.izquierda = None
        self.data = value
        self.derecha = None

class Arbol:
   
    def crearNodo(self, data):
        return Nodo(data)

    def insertar(self, nodo , data):
        if nodo is None:
            return self.crearNodo(data)
        if data < nodo.data:
            nodo.izquierda = self.insertar(nodo.izquierda, data)
        elif data > nodo.data:
            nodo.derecha = self.insertar(nodo.derecha, data)

        return nodo


    def buscar(self, nodo, data):
        if nodo is None or nodo.data == data:
            return nodo

        if nodo.data < data:
            return self.buscar(nodo.derecha, data)
        else:
            return self.buscar(nodo.izquierda, data)



    def eliminarNodo(self,nodo,data):
        if nodo is None:
            return None

        if data < nodo.data:
            nodo.izquierda = self.eliminarNodo(nodo.izquierda, data)
        elif data > nodo.data:
            nodo.derecha = self.eliminarNodo(nodo.derecha, data)
        else:
            if nodo.izquierda is None and nodo.derecha is None:
                del nodo
            if nodo.izquierda == None:
                temp = nodo.derecha
                del nodo
                return  temp
            elif nodo.derecha == None:
                temp = nodo.izquierda
                del nodo
                return temp

        return nodo


    def transversaEnOrden(self, raiz):
        if raiz is not None:
            self.transversaEnOrden(raiz.izquierda)
            print raiz.data
            self.transversaEnOrden(raiz.derecha)

    def transversaEnPreorden(self, raiz):
        if raiz is not None:
            print raiz.data
            self.transversaEnPreorden(raiz.izquierda)
            self.transversaEnPreorden(raiz.derecha)

    def transversaEnPostorden(self, raiz):
        if raiz is not None:
            self.transversaEnPreorden(raiz.izquierda)
            self.transversaEnPreorden(raiz.derecha)
            print raiz.data


def main():
    raiz = None
    arbol = Arbol()
    raiz = arbol.insertar(raiz, 10)
    print raiz
    arbol.insertar(raiz, 20)
    arbol.insertar(raiz, 30)
    arbol.insertar(raiz, 40)
    arbol.insertar(raiz, 70)
    arbol.insertar(raiz, 60)
    arbol.insertar(raiz, 80)

    print "transversa en ornden"
    arbol.transversaEnOrden(raiz)

    print "transversa en preorden"
    arbol.transversaEnPreorden(raiz)

    print "transversa en postorden"
    arbol.transversaEnPostorden(raiz)


if __name__ == "__main__":
    main()
