#Es crea una classe
class Car:
    #Es crea un constructor amb 4 atributs per crear 
    # instàncies de la classe
    def __init__(self,matricula,color,pes,marca):
        self.matricula = matricula
        self.color = color
        self.pes = pes
        self.marca = marca
    
    #Definició dels getters, serveixen per obtenir 
    #el valor dels atributs de les instàncies

    def getMatricula(self):
        return self.matricula
    def getColor(self):
        return self.color
    def getPes(self):
        return self.pes
    def getMarca(self):
        return self.marca
    
    #Definició dels setters, serveixen
    #per modificar el valor dels atributs de les instàncies  

    def setMatricula(self,matricula):
        self.matricula = matricula
    def setColor(self,color):
        self.color = color   
    def setPes(self,pes):
        self.pes = pes
    def setMarca(self,marca):
        self.marca = marca
    
    #Definició del mètode que imprimeix els atributs 
    # de l'objecte
    def salutacio(self):
        print("La matricula del cotxe és: " +self.matricula+
              "\nEl color és: " +self.color+ "\nEl pes és: "
              +str(self.pes)+ "\nLa marca és: " +self.marca)
    
    #Mètode que retorna un diccionari de la classe en format
    #diccionari
    def to_dict(self):
        return {
            "matricula":self.matricula,
            "color":self.color,
            "pes":self.pes,
            "marca":self.marca
        }