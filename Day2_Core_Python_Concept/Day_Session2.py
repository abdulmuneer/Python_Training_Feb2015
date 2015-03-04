# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# __Class__

# <codecell>

class Circle :
    def __init__(self, rad):
        self.radius = rad
    
    def __area(self):
        return 3.14*self.radius*self.radius
        
    

circle1 = Circle(10)
circle2 = Circle(20)
#adding a new attribute to an object
circle1.colour = "Blue"

print circle1.colour
print dir(circle1)
print dir(circle2)
print circle2.colour

#dir(circle1)

# <codecell>

print circle1.__dict__
print Circle.__dict__

# <codecell>

class Vehicle(object):
    def __init__(self, speed, number, color):
        self.speed = speed
        self.number = number
        self.color = color
        
    def start(self):
        print "Starting"
        
    def stop(self):
        print "Stopping"
    
    def accelerate(self):
        print "accelerating"
        
    def break_(self):
        print "breaking.."
        

# <codecell>

class Plane(Vehicle):
    #def __init__(self, speed, number, color ):
     #   Vehicle.__init__(self, speed, number, color )
    def fly(self):
        print "Flying"
        
    def break_(self):
        print "You can't break in mid-air"
    
    def start(self):
        #Vehicle.start(self)
        super(Plane, self).start()
        print "Taking Off"
    
    

# <codecell>

plane = Plane(300, 707, 'blue')
plane.start()
#print plane.color
#plane.break_()

# <markdowncell>

# __New Style and Old Style classes:__

# <markdowncell>

# * new style classes inherit from a class called 'object' 

# <codecell>

dir(Circle)

# <codecell>

dir(Vehicle)

