erste_stufe = 7

def outer():
    zweite_stufe = 5
    
    def inner():
        dritte_stufe = 6

        print("erste_stufe=", erste_stufe)
        print("zweite_stufe=", zweite_stufe)
        print("dritte_stufe=", dritte_stufe)
    inner()
    
    print("erste_stufe=", erste_stufe)
    print("zweite_stufe=", zweite_stufe)
    print("dritte_stufe=", dritte_stufe)
outer()

print("erste_stufe=", erste_stufe)
print("zweite_stufe=", zweite_stufe)
print("dritte_stufe=", dritte_stufe)