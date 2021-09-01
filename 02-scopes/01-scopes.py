x = 7

def outer():
    y = 5
    
    def inner():
        z = 6

        print("x=", x)
        print("y=", y)
        print("z=", z)
    inner()
    
    print("x=", x)
    print("y=", y)
    print("z=", z)
outer()

print("x=", x)
print("y=", y)
print("z=", z)