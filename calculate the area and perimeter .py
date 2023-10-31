#calculate the area and perimeter 


class Shape:
    @classmethod
    def calculate_area(cls, measurements):
        # Implement the calculation of the area based on the measurements
        # Example for a rectangle: area = length * width
        return measurements[0] * measurements[1]

    @classmethod
    def calculate_perimeter(cls, measurements):
        # Implement the calculation of the perimeter based on the measurements
        # Example for a rectangle: perimeter = 2 * (length + width)
        return 2 * (measurements[0] + measurements[1])

# Example usage:
rectangle_measurements = [5, 8]  # Length and width of a rectangle
area = Shape.calculate_area(rectangle_measurements)
perimeter = Shape.calculate_perimeter(rectangle_measurements)

print(f"Area: {area}")
print(f"Perimeter: {perimeter}")