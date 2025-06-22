## Shape Calculator - Rectangle and Square Operations
This Python project, created as part of freeCodeCamp's scientific computing curriculum, implements a ```Rectangle``` class and a ```Square``` subclass to explore geometric behavior through object-oriented programming. It allows users to set dimensions, retrieve shape properties, print simple visual representations, and calculate how many times one shape can fit inside another.

## Features
- Create rectangles or squares with specified dimensions
- Update width, height, or side values dynamically
- Calculate key geometric properties: area, perimeter, and diagonal length
- Display ASCII-style visual representations of shapes
- Determine how many times a smaller shape can fit inside a larger one

## Usage
### Create a rectangle
```rect = Rectangle(10, 5)
print(rect.get_area())             # Outputs area
rect.set_height(3)                 
print(rect.get_perimeter())        # Outputs perimeter
print(rect)                        # String representation
print(rect.get_picture())          # ASCII picture of rectangle
```

### Create a square
```sq = Square(9)
print(sq.get_area())               # Outputs area
sq.set_side(4)                     
print(sq.get_diagonal())           # Outputs diagonal length
print(sq)                          # String representation
print(sq.get_picture())            # ASCII picture of square
```

### Fit shape inside another
```rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))  # How many times square fits in rectangle
```

## Example Output
```50
26
Rectangle(width=10, height=3)
**********
**********
**********

81
5.656854249492381
Square(side=4)
****
****
****
****

8                                                                 
```

## Project Goal
This project focuses on reinforcing object-oriented programming principles such as inheritance, encapsulation, and method overriding. It also demonstrates:

- Writing and organising class-based code in Python
- Applying geometric formulas to compute properties
- Generating simple ASCII-based output
- Using custom ```__str__``` methods for clean printing
- Designing subclass behavior that extends or modifies the base class

It forms part of a broader journey into Python development, laying the foundation for future work in areas like data visualisation, simulation, and design tools.


