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
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        # Creates a string of '*' characters
        line = "*" * self.width + "\n"
        return line * self.height

    def get_amount_inside(self, shape):
        # Calculates how many times another shape fits inside this one
        horizontal = self.width // shape.width
        vertical = self.height // shape.height
        return horizontal * vertical

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, side):
        # A square is just a rectangle where width and height are the same
        super().__init__(side, side)

    def set_side(self, side):
        self.width = side
        self.height = side

    # Overriding these to ensure width and height stay identical
    def set_width(self, side):
        self.set_side(side)

    def set_height(self, side):
        self.set_side(side)

    def __str__(self):
        return f"Square(side={self.width})"
