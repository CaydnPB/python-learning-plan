import math

class Circle:
    
    PI = math.pi
    
    def __init__(self, radius):
        self.radius = radius
        self.area = self.PI*(self.radius**2)
        self.diameter = self.radius*2
        self.circumference = self.PI*self.diameter
        self.output()
       
    def output(self):
        decision = input("Would you like to view rounded values?\nEnter [Y] or [N]:\n")
        if decision.upper() == "Y":
            print("Generating rounded values...")
            print("Radius:",round(self.radius),"\nArea:",round(self.area),"\nDiameter:",round(self.diameter),"\nCircumference:",round(self.circumference),"\nPI:",round(self.PI))
        elif decision.upper() == "N":
            print("Generating unrounded values...")
            print("Radius:",self.radius,"\nArea:",self.area,"\nDiameter:",self.diameter,"\nCircumference:",self.circumference,"\nPi:",self.PI)
        else:
            print("Invalid response; please try again!")
            self.output()

def main():
    choice = input("Welcome to OOP Circle!\n----------------------\nR: Enter radius\nQ: Quit\nEnter [R] or [Q]:\n")
    if choice.upper() == "Q":
        exit()
    elif choice.upper() == "R":
        pass
    else:
        print("Invalid response; please try again!")
        main()
    radiusnum = False
    while radiusnum == False:
        radius = input("Enter the radius of your circle:\n")
        if radius.isnumeric() == True:
            radius = int(radius)
            radiusnum = True
        else:
            print("Invalid response; please try again!")
            radiusnum = False
    circle = Circle(radius)

main()
