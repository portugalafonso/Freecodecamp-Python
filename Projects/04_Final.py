class Rectangle:
    #it has to be  initialized with width and height attributes.
    def __init__(self, width_input, height_input):
        self.width = int(width_input)
        self.height = int(height_input)

    #If represented as a string: Rectangle(width=5, height=10)
    def __str__(self):
        return "Rectangle(width={}, height={})".format(self.width, self.height)
        
    def set_width(self, width_input):
        self.width = int(width_input)

    def set_height(self, height_input):
        self.height = int(height_input)

    def get_area(self):
        return (self.width * self.height)


    def get_perimeter(self):
        return (2*self.width + 2*self.height)

    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** .5)

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        picture_string = ""
        i = 0
        while i != self.height:
            picture_string = picture_string + "*"*self.width+"\n"
            i += 1
        return picture_string
    
    def get_amount_inside(self, shape):
        return int(self.get_area() / shape.get_area())
   
        
class Square(Rectangle):
    def __init__(self, side_input):
        self.side = side_input
        self.height = side_input
        self.width = side_input
    #If represented as a string: # Square(side=9)
    def __str__(self):
       return "Square(side={})".format(self.width)
       # Square(side=9)

    def set_side(self, side_input):
        self.width = int(side_input)
        self.height = int(side_input)
    
    def set_width(self, side_input):
        self.set_side(side_input)

    def set_height(self, side_input):
        self.set_side(side_input)

rect = Rectangle(10, 5)
sq = Square(9)
sq.set_side(4)
rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))