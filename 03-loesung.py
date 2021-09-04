from turtle import *

def rect(laenge):
    for ii in range(2):
        forward(laenge)
        right(90)
        forward(laenge)
        right(90)

def dach(laenge):
    for jj in range(3):
        forward(laenge)
        right(120)

def change_pos(laenge, back):
    if back:
        left(30)
        backward(laenge)
    else:
        forward(laenge)
        right(30)

def haus(laenge):
    rect(laenge)
    change_pos(laenge, back=False)
    dach(laenge)
    change_pos(laenge, back=True)

def strasse(laenge, num_hauss):
    for kk in range(num_hauss):
        haus(laenge)
        
        right(90)
        forward(laenge)
        left(90)
        
        laenge += 20

    return laenge

def main():
    left(90)
    speed(100000)

    laenge = 100

    
    laenge = strasse(laenge, 5)

    haus(laenge)
    done()

if __name__ == "__main__":
    main()