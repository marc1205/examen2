
dic ={ open("results.json", mode="rt", encoding="utf-8") }

def search_by_lon(k,l,dic) :
    for i in dic :
        if k == l[i] :
            lista = lista[i](k,l)
            return lista
        
    for i in lista:
        if lista[i] < 0 :
            raise ValueError("No existe")
        if lista[i] != type(float) :
            
