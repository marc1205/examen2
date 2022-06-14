
read_data = open("stops.csv", mode="rt", encoding="utf-8")
read_data2 = open("stops_data.csv", mode="rt", encoding="utf-8")

dic = read_data.read()
dic2 = read_data2.read()  

dicFinal = {
    "Clave" : dic[0],
    'id' : dic[0],
    'lat' : dic2[4],
    'lon' : dic2[5],
    'name' : dic[2]
}

