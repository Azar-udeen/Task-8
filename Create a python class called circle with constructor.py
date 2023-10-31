#Create a python class called circle with constructor


class Circle:
    def _init_(self, radius_list):
        self.radius_list = radius_list

# Example usage
radius_list = [10, 501, 22, 37, 100, 999, 87, 351]
circle = Circle(radius_list)

# Access the list through the instance variable
print(circle.radius_list)