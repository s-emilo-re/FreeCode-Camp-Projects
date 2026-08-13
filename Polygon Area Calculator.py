import math

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height
    
    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2 * (self.width + self.height)
    
    def get_diagonal(self):
        return math.sqrt(self.width**2 + self.height**2)
    
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        
        picture = ""
        for _ in range(self.height):
            picture += "*" * self.width + "\n"
        return picture
    
    def get_amount_inside(self, shape):
        width_fit = self.width // shape.width
        height_fit = self.height // shape.height
        return width_fit * height_fit
    
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.side = side
    
    def set_side(self, side):
        self.side = side
        self.width = side
        self.height = side
    
    def set_width(self, width):
        self.set_side(width)
    
    def set_height(self, height):
        self.set_side(height)
    
    def __str__(self):
        return f"Square(side={self.side})"


# Test the code with the example from the problem
if __name__ == "__main__":
    print("Testing Rectangle and Square classes:\n")
    
    rect = Rectangle(10, 5)
    print(f"Rectangle area: {rect.get_area()}")  # 50
    rect.set_height(3)
    print(f"Rectangle perimeter: {rect.get_perimeter()}")  # 26
    print(f"Rectangle string: {rect}")  # Rectangle(width=10, height=3)
    print("Rectangle picture:")
    print(rect.get_picture())  # 10 * lines, 3 rows
    
    print("\n" + "-"*30 + "\n")
    
    sq = Square(9)
    print(f"Square area: {sq.get_area()}")  # 81
    sq.set_side(4)
    print(f"Square diagonal: {sq.get_diagonal()}")  # 5.656854249492381
    print(f"Square string: {sq}")  # Square(side=4)
    print("Square picture:")
    print(sq.get_picture())  # 4 * lines, 4 rows
    
    print("\n" + "-"*30 + "\n")
    
    rect.set_height(8)
    rect.set_width(16)
    print(f"Rectangle after resize: {rect}")
    print(f"Square after resize: {sq}")
    print(f"How many squares fit in rectangle: {rect.get_amount_inside(sq)}")  # 8
    
    print("\n" + "-"*30 + "\n")
    
    # Additional tests
    print("Testing too big picture:")
    big_rect = Rectangle(60, 5)
    print(big_rect.get_picture())  # "Too big for picture."
    
    print("\nTesting amount inside:")
    rect1 = Rectangle(15, 10)
    sq1 = Square(5)
    print(f"Rectangle(15,10) inside Square(5): {rect1.get_amount_inside(sq1)}")  # 6
    
    rect2 = Rectangle(4, 8)
    rect3 = Rectangle(3, 6)
    print(f"Rectangle(4,8) inside Rectangle(3,6): {rect2.get_amount_inside(rect3)}")  # 1
    
    rect4 = Rectangle(2, 3)
    rect5 = Rectangle(3, 6)
    print(f"Rectangle(2,3) inside Rectangle(3,6): {rect4.get_amount_inside(rect5)}")  # 0