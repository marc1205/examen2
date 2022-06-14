
dic ={ open("results.json", mode="rt", encoding="utf-8") }

def get_min(k,d) :
    for i in dic :
        if k > d[i] :
            lista = lista[i](k,d)
            return lista
        
    for i in lista:
        if lista[i] < 0 :
            raise ValueError("No hay elementos")

    
