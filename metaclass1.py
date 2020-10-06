class Foo:
    def show(self):
        print("hi")

def add_attribute(self):
    self.z = 9
    

Test = type('Test',(Foo,),{"x":5, "add_attribute": add_attribute})

t= Test()
t.wy ="Hello"
t.add_attribute()
print(t.z)
t.show()

print(Test)
print(Test())
print(type(Test()))
print(type(2))
print(type(int))
print(type(Test))

