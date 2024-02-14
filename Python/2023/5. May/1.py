def greet(fx):
    def mfx():
        print("Good morning")
        fx()
        print("Thanks for using this function")
        return mfx

@greet
def hello():
    print("Hello world")

@greet
def add(a, b):
    print(a+b)
hello()
add(3,4)