#Importar les classes de la subcarpeta
from IntegrantA.Car import Car
from IntegrantA.animal import animal
#Importar llibreria json
import json

#Crear una llista de 2 elements per cada clase creada
#Cada element és una instància
cars = [Car("44553R","blau",800,"Ford"),
        Car("55332E","groc",900,"Fiat")]
animals = [animal("gat",4,"mamifer",0.3),
           animal("colibri",1,"ocell",0.1)]

#Coverteix la llista d'instàncies a un diccionari 
# amb el mpetode to_dict
cars_list =[car.to_dict() for car in cars ]
animals_list = [animal.to_dict() for animal in animals]

#Guardar llistes en objecte contenidor
data = {"cars":cars_list,"animals":animals_list}

#Guarda l'objecte contenidor en un fitxer
with open("json_API/a.json",'w') as file:
    json.dump(data,file)

