
def consulta_tipo_sangre(function):
    def wrapper(tipo_de_sangre):
        if tipo_de_sangre == "O-":
            print("puede recibir sangre de O-")
        elif tipo_de_sangre == "O+":
            print("puede recibir sangre de O+ y 0-")
        elif tipo_de_sangre == "A+":
            print("puede recibir sangre de O+, O-, A+ y A-")
        elif tipo_de_sangre == "A-":
            print("puede recibir sangre de O- y A-")
        elif tipo_de_sangre == "B+":
            print("puede recibir sangre de O+, O-, B+ y B-")
        elif tipo_de_sangre == "B-":
            print("puede recibir sangre de O- y B-")
        elif tipo_de_sangre == "AB+":
            print("puede recibir sangre de todos los tipos ")
        elif tipo_de_sangre == "AB-":
            print("puede recibir sangre de AB-, A-, B- y O-")
        else:
            print("Por favor ingrese un tipo de sangre valido")
            return function(tipo_de_sangre)
    return wrapper

