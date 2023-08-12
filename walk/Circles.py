class Circle:

    circles = []

    def __init__(self, center, radius):
        self.center = center
        self.radius = radius
        # self.circles.append(self)
        if not Circle.if_intersecting(center, radius, Circle.circles):  # Correct method call and logic
            Circle.circles.append(self)
            # Circle.circles.pop()  # Remove the circle if it's not valid

    def __str__(self):
        return f"{self.center}({self.radius})"

    @staticmethod
    def if_intersecting(center, radius, circle_list):
        for item in circle_list:
            # Calculate the distance between centers using the distance formula
            distance = ((center[0] - item.center[0])**2 + (center[1] - item.center[1])**2)**0.5
            if distance <= radius + item.radius:
                return True  # Circles intersect
        return False  # Circles do not intersect

