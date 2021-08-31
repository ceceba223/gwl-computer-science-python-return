from turtle import *

def rect(lenght):
    for ii in range(2):
        forward(lenght)
        right(90)
        forward(lenght)
        right(90)

def roof(lenght):
    for jj in range(3):
        forward(lenght)
        right(120)

def change_pos(lenght, back):
    if back:
        left(30)
        backward(lenght)
    else:
        forward(lenght)
        right(30)

def house(lenght):
    rect(lenght)
    change_pos(lenght, back=False)
    roof(lenght)
    change_pos(lenght, back=True)

def street(lenght, num_houses):
    for kk in range(num_houses):
        house(lenght)
        
        right(90)
        forward(lenght)
        left(90)
        
        lenght += 20
        lenght += 20

    return lenght

def main():
    left(90)
    speed(100000)

    lenght = 100
    lenght = 50
    
    lenght = street(lenght, 5)

    house(lenght)
    done()

if __name__ == "__main__":
    main()