class Class_method:
    a= 10
    
    @classmethod        #By using Class_method  it shows the class value 
    def show (cls):
        print(f"the vlaue a is {cls.a} ")
        
    @property           # create like property but it is not a property when ever you create property the use Setter with function name
    def name(self):
        return f"{self.fname} or {self.lname}"
    
    @name.setter        # the property refer to set the @property value 
    def name(self,value):
        self.fname=value.split(" ")[0]
        self.lname=value.split(" ")[1]
        
c=Class_method()

c.name= "hello ammar"
print(c.name)

c.show()
