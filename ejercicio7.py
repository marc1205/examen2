
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
        for i in dic:
            res =("Clave", i, "valor", dic[i])
            return res
        print(res)
    

