class Boundary:
    def __init__(self, point1, point2, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.x1 = point1.x
        self.x2 = point2.x
        self.y1 = point1.y
        self.y2 = point2.y
        self.a, self.b = self.update_linear_factors()

    def update_linear_factors(self):
        if self.x1 != self.x2:
            a = (self.y2 - self.y1) / (self.x2 - self.x1)
            b = self.y1 - a * self.x1
        else:
            a = None
            b = None
        return a, b

    def __str__(self):
        return_string = f"x1: {self.x1}, y1: {self.y1}, x2: {self.x2}, y2: {self.y2}, a: {self.a}, b: {self.b}"
        return return_string
