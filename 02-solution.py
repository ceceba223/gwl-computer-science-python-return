from turtle import *

def rect(height, width):
    for ii in range(2):
        forward(height)
        right(90)
        forward(width)
        right(90)

def roof(width):
    for jj in range(3):
        forward(width)
        right(120)

def change_pos(height, back):
    if back:
        left(30)
        backward(height)
    else:
        forward(height)
        right(30)

def house(height, width):
    rect(height, width)
    change_pos(height, back=False)
    roof(width)
    change_pos(height, back=True)

def street(height, width, num_houses):
    for kk in range(num_houses):
        house(height, width)
        
        right(90)
        forward(width)
        left(90)
        
        height += 20
        width += 20
    return height, width

def main():
    left(90)
    speed(100000)

    height = 100
    width = 50
    
    height, width = street(height, width, 5)

    house(height, width)
    done()

if __name__ == "__main__":
    main()