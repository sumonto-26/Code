class Animal() :

    def hello(self):
        self.a = "hello world"
        # return self.a
        print(self.a)

class Zoo (Animal):

    def world(self):
        self.b = "animal zoo"
        return self.b


obj = Zoo()
obj.hello()
# print(obj)
