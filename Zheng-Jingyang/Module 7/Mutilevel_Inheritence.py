class Animal:
    def _init_(self,name):
        self.name = name
    
    def getName(self):
        return self.name

class Dog(Animal):
    def _init_(self, name, age):
        Animal._init_(self,name)
        self.age = age 
    
    def getAge(self):
        return self.age

class pug(Dog):
    def _init_(self,name, age,color):
        Dog._init_(self,name,age)
        self.color = color

    def getColor(self):
        return self.color

ob = pug("PugPug",2, "Brown")
print(ob.getName(), ob.getAge(), ob.getColor())
