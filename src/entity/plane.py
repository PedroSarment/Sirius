from ..geometry.vector import Vector
from ..graphic.color import Color
from ..geometry.ray import Ray

class Plane:
    def __init__(self, point: Vector, normal: Vector, color: Color):
        self.point = point
        self.normal = normal
        self.color = color

    def intersect(self, ray: Ray):
        direction_dot_normal = ray.direction.dot(self.normal)

        if abs(direction_dot_normal) < 1e-6:
            return {
                "color": Color(0, 0, 0),
                "distance": float('inf'),
                "normal": None #TODO: Calcular normal
            }

        t = self.point.sub(ray.point).dot(self.normal) / direction_dot_normal

        return {
                "color": self.color,
                "distance": t,
                "normal": None #TODO: Calcular normal
            } if t >= 0 else {
                "color": Color(0, 0, 0),
                "distance": float('inf'),
                "normal": None #TODO: Calcular normal
            }