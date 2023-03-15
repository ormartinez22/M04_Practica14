class animal:#Definició de la classe

    #Definició del mètode que imprimeix els atributs de l'objecte
    def salutacio(self):
        print("El nom de l'animal és: " +self.nom)
        print("L'edat és: " +str(self.edat))
        print("El tipus és: " +self.tipus)
        print("L'altura és: " +str(self.altura))
        
    
    #Definicio del constructor amb 6 atributs, serveix per crear instancies de classe
    def __init__(self,nom,edat,tipus,altura):
        self.nom = nom
        self.edat = edat
        self.tipus = tipus
        self.altura = altura

    #Definició dels getters, serveixen per obtenir el valor dels atributs de les instàncies
    def getNom(self):
        return self.nom
    def getEdat(self):
        return self.edat
  
    #Definició dels setters, serveixen per modificar el valor dels atributs de les instàncies  
    def setNom(self, nom):
        self.nom = nom
    def setEdat(self, edat):
        self.edat = edat
    def setTipus(self, tipus):
        self.tipus = tipus
    def setAltura(self, altura):
        self.altura = altura
    
    def to_dict(self):
        return {
            "nom":self.nom,
            "color":self.edat,
            "pes":self.tipus,
            "marca":self.altura
        }
  
