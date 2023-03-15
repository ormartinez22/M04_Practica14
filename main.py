#Importar les classes de la subcarpeta
from IntegrantA.Car import Car
from IntegrantA.animal import animal

from INTEGRANT_B.Cat import Cat
from INTEGRANT_B.university import university
#Importar llibreria json
import json

#Crear una llista de 5 elements per cada clase creada
#Cada element és una instància

cars = [Car("44553R","blau",800,"Ford"),
        Car("55332E","groc",900,"Fiat"),
        Car("11132E","verd",1000,"BMW"),
        Car("55662E","gris",700,"Citroen"),
        Car("55552E","marro",800,"Seat")]

animals = [animal("gat",4,"mamifer",0.3),
           animal("colibri",1,"ocell",0.1),
           animal("lleo",6,"mamifer",0.5),
           animal("serp",1,"reptil",0.1),
           animal("cocodril",4,"anfibi",0.3)]

cats = [Cat("tom","2","persian","brown"),
       Cat("ginger","5","Exotic","white"),
       Cat("perl","6","American","black"),
       Cat("melissa","1","British","greenish Black"),
       Cat("angela","3","Siames","mustard")
    
       ]
universities = [university("uab","sud","Sant Cugat","medicina"),
       university("upc","nord","Barcelona","enginyeria"),
       university("ub","est","Barcelona","filosofia"),
       university("Pompeu Fabra","oest","Barcelona","quimica"),
       university("Harvard","north","California","tourism")
    
       ]

#Coverteix la llista d'instàncies a un diccionari 
# amb el mpetode to_dict
cars_list =[car.to_dict() for car in cars ]
animals_list = [animal.to_dict() for animal in animals]

cats_list =[cat.to_dict() for cat in cats ]
universities_list = [university.to_dict() for university in universities]

#Guardar llistes en objecte contenidor
data = {"cars":cars_list,"animals":animals_list}
datas = {"cats":cars_list,"universities":animals_list}

#Guarda l'objecte contenidor en un fitxer
with open("json_API/a.json",'w') as file:
    json.dump(data,file)

with open("json_API/b.json",'w') as file:
    json.dump(datas,file)
