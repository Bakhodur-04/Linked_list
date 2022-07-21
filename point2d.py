class Point2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, num):
        point_x = self.x + num
        point_y = self.y + num
        return point_x, point_y

    def __str__(self):
        return f"{str(self.x)}, {str(self.y)}"

    def __mul__(self, num):
        point_x = self.x * num
        point_y = self.y * num
        return point_x, point_y

    def __sub__(self, num):
        point_x = self.x - num
        point_y = self.y - num
        return point_x, point_y

    def __sub_add__(self, num):
        point_x = self.x - num
        point_y = self.y + num
        return point_x, point_y

    def __add_sub__(self, num):
        point_x = self.x + num
        point_y = self.y - num
        return point_x, point_y
