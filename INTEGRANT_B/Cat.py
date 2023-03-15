#creating a class Cat
class Cat:
    #making a method to define the self attributes of the class
    def info(self):
      #printing all attributes one by one
      print("The name of the cat is : " + self.name) 
      print("The breed of the cat is : " + self.breed)
      print("The age of the cat is : " + self.age)
      print("The color of the cat is : " + self.color)

#making the constructors or builders of the given class
    def __init__(self,name,breed,age,color):
        #difining all the attributes of the constructor one by on
        self.name = name
        self.breed = breed
        self.age = age
        self.color = color   

#difining getter method for name
    def getName(self):
           return self.name


#difining setter method for name    
    def setName(self , name):
         self.name = name

#difining getter method for breed
    def getBreed(self):
       return self.breed


#difining setter method for breed    
    def setBreed(self , breed):
     self.breed = breed

#difining getter method for age
    def getAge(self):
      return self.age


#difining setter method for age    
    def setAge(self , age):
     self.age = age

#difining getter method for color
    def getColor(self):
       return self.color


#difining setter method for color
    def setColor(self , color):
       self.color = color

    def to_dict(self):
       return {
          "name":self.name,
          "breed":self.breed,
          "age":self.age,
          "color":self.color
       }