# LegoBrickClass.py

from graphics import *

class LegoBrick:
    # constructor
    def __init__(self, win, lowerLeftCorner, length, color):
        self.win = win
        self.color = color
        self.lengthIn = length

        # create internal represention
        self.x = lowerLeftCorner.getX()
        self.y = lowerLeftCorner.getY()
        self.length = length * 7.5
        self.height = length * 2.5
        self.nibLen = length * 0.75
        self.nibHgt = length * 0.3
        self.nibXOffset = length * 0.375
        self.nibYOffset = self.height        
        self.myObjs = []

        # create brick body
        body = Rectangle(lowerLeftCorner,
                         Point(self.x+self.length, self.y+self.height))
        body.setWidth(3)
        self.myObjs.append(body)

        # create first nib
        nib = Rectangle(Point(self.x + self.nibXOffset, self.y + self.height),
                        Point(self.x + self.nibXOffset + self.nibLen,
                              self.y + self.height + self.nibHgt))
        nib.setWidth(3)
        self.myObjs.append(nib)

        # create the rest of the nibs using cloning
        for i in range(1, 5):
            nibTemp = nib.clone()
            nibTemp.move(self.nibXOffset * 4 * i, 0)
            self.myObjs.append(nibTemp)

        # set fill color
        self.setFill(self.color)

    def setFill(self, color):
        self.color = color
        for obj in self.myObjs:
            obj.setFill(color)

    def draw(self, win):
        for obj in self.myObjs:
            obj.draw(win)

    def clone(self):
        newBrick = LegoBrick(self.win, Point(self.x, self.y), self.lengthIn, self.color)
        return newBrick

    def move(self, xOffset, yOffset):
        for obj in self.myObjs:
            obj.move(xOffset, yOffset)

def main():
    win = GraphWin("Lego Bricks", 500, 375)
    win.setCoords(0.0, 0.0, 20.0, 15.0)
    win.setBackground("light gray")

    brick1 = LegoBrick(win, Point(1, 1), 1, "blue")
    brick1.draw(win)

    brick2 = brick1.clone()
    brick2.setFill("black")
    brick2.move(8.5, 0)
    brick2.draw(win)

    brick3 = brick1.clone()
    brick3.setFill("yellow")
    brick3.move(0, 4)
    brick3.draw(win)
    
    win.getMouse()

main()    