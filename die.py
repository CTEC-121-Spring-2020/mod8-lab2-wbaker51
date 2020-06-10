# die.py

from graphics import *

class Die:
    # constructor
    def __init__(self, win, center, size):
        #print("die created")

        # instance variables
        self.win = win
        self.value = 1
        self.background = "white"

        # create the square for the face

        # need to do calculations from the center
        halfSize = size/2.0

        # create square
        p1 = Point(center.getX() - halfSize, center.getY() - halfSize)
        p2 = Point(center.getX() + halfSize, center.getY() + halfSize)
        rect = Rectangle(p1, p2)
        rect.setFill(self.background)
        rect.draw(win)

# unit test
def dieTest():
    win = GraphWin("Dice Roller", 500, 500)
    win.setCoords(0, 0, 10, 10)
    win.setBackground("green2")
    d = Die(win, Point(3,7), 2)

    win.getMouse()

if __name__ == '__main__':
    dieTest()