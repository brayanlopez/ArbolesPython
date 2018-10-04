class Nodo():
        def __init__ (self,raiz=0,izq=None,der=None):
                self.izq=izq
                self.der=der
                self.raiz=raiz

def buscarEnArbol(arbol,valor):
        if arbol == None:
                return False
        if (valor == arbol.raiz):
                return True
        if(valor>arbol.raiz):
                return buscarArbol(arbol.der,valor)
        return buscarArbol(arbol.izq,valor)

def contarNodos(arbol,a=0):
        if(arbol.izq==None and arbol.der==None):
                return a+0
        if(arbol.izq!=None or arbol.der!=None):
                a+1
                a += contarNodos(arbol.izq,a) + contarNodos(arbol.der,a)
                return a

def contarHojas(arbol,valor):
        pass

def contarElementos(arbol,valor):
        pass

def insertarElemento(arbol,valor):
        if arbol == None:
                return Nodo(valor)
        if valor < arbol.raiz:
                return Nodo(arbol.raiz, insertarElemento(arbol.izq,valor) , arbol.der)
        return Nodo(arbol.raiz, arbol.izq, insertarElemento(arbol.der,valor))

def preOrden(arbol):
     if arbol == None:
        return []
     else:
        return [arbol.raiz] + preOrden(arbol.izq) + preOrden(arbol.der)

def posOrden(arbol):
    if arbol == None:
        return []
    else:
        return posOrden(arbol.izq) + posOrden(arbol.der) + [arbol.raiz]

def inOrden(arbol):
    if arbol == None:
        return []
    else:
        return inOrden(arbol.izq) + [arbol.raiz] + inOrden(arbol.der)


nodoA = Nodo(10,Nodo(1),Nodo(13))
nodoB = Nodo(30,nodoA, Nodo(40))
nodoC = Nodo(4, nodoA, nodoB)

nodoP = Nodo (0,nodoA, nodoB)


#print (buscarArbol(nodoC,1))

print (preOrden(nodoP))

print (posOrden(nodoP))

print (inOrden(nodoP))

print (insertarElemento(nodoP,5))
