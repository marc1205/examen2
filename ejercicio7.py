
class Stop:
    def __init__(self, id, name, description, lat, lon) :
        self.__i = id
        self.__n = name
        self.__d = description
        self.__lt = lat
        self.__ln = lon
    
    def to_string(self) :
        i = str(self.__i),
        n = str(self.__n),
        d = str(self.__d),
        lt = str(self.__lt),
        ln = str(self.__ln),
        return i,n,d,lt,ln

    def convert_to_object(self, clave, dic) :
        for i in clave:
            res =("Clave", i, "valor", dic[i])
        Stop = Stop(res)
        return Stop


dic = open("results.json", mode="rt", encoding="utf-8")
clave = 1080
res = Stop.convert_to_object(clave,dic)

resultado = Stop.to_sring(res)
    


