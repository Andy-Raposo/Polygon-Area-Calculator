class Rectangle:
    '''Represents a rectangle with width and height.'''

    width: int
    height: int
    type: str

    def __init__(self, width, height):
        # Initialises the rectangle's width and height attributes
        self.width = width
        self.height = height
    
    def __init_subclass__(cls):
        # Ensures that all subclasses define a 'type' attribute at the beginning
        if not hasattr(cls, 'type'):
            raise AttributeError(f'Class type of {cls.__name__} is missing.')
    
    def set_width(self, width):
        # Set the width of the rectangle
        self.width = width
    
    def set_height(self, height):
        # Set the height of the rectangle
        self.height = height
    
    def get_area(self):
        # Calculates and returns the area of the rectangle
        return self.width * self.height
    
    def get_perimeter(self):
        # Calculates and returns the perimeter of the rectangle
        return (2 * self.width) + (2 * self.height)

    def get_diagonal(self):
        # Calculates and returns the diagonal length through the Pythagoras theorem
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        # Returns a string picture of the rectangle using '*', filled
        # If any of the sides are over 50 in length, return a message
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        picture = ''
        for _ in range(self.height):
            picture += self.width * '*' + '\n'
        return picture
    
    def get_amount_inside(self, shape2):
        # Calculates how many times a second rectangle (shape2) can fit inside this first rectangle
        width1, height1 = self.width, self.height
        width2, height2 = shape2.width, shape2.height
        times_fits_width = 0
        times_fits_height = 0
        if width1 < width2:
            return 0
        if height1 < height2:
            return 0
        
        times_fits_width += width1 // width2
        times_fits_height += height1 // height2
            
        return times_fits_width * times_fits_height

    def __str__(self):
        # String representation of the rectangle object
        return f"Rectangle(width={self.width}, height={self.height})"

class Square(Rectangle):
    '''Represents a square, subclass of Rectangle, with equal sides.'''
    type = 'square'

    def __init__(self, side):
        # Initialises a square with all sides equal to 'side'
        self.width = side
        self.height = side

    def __str__(self):
        # String representation of the square object
        return f"Square(side={self.width})"

    def set_side(self, side):
        # Sets both width and height to the same side length
        self.width = side
        self.height = side

    def set_width(self, width):
        # Overrides set_width to keep the square's sides equal
        self.set_side(width)
    
    def set_height(self, height):
        # Overrides set_height to keep the square's sides equal
        self.set_side(height)

    def get_picture(self):
        # Returns a string picture of the square using '*'
        # If any of the sides are over 50 in length, then return a message
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        picture = ''
        for _ in range(self.height):
            picture += self.width * '*' + '\n'
        return picture