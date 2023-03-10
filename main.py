import shape_calculator
from unittest import main

rect = shape_calculator.Rectangle(10, 13)
print(rect.get_area())
rect.set_width(3)
print(rect.get_perimeter())
print(rect)

sq = shape_calculator.Square(20)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)

# Run unit tests automatically
main(module='test_module', exit=False)
