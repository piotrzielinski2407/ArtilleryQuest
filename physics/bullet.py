from math import radians, cos, sin
from geometry import Geometry
from point import Point
from universal_object import UniversalObject


class Bullet(UniversalObject):
    """
    Class that will calculate bullet movement in time from fire moment to hit the ground, movement will be pass
    by a tuple with coordinates x, y, where x is horizontal and y is vertical position.
    Starting point will be by default in the middle of artillery truck.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # declare here only bullet object properties
        self.bullets_config = self.load_config_file("bullets_config.json")
        self.mass = None
        self.x_drag_coef = None  # drag coefficient of bullet in x dir (from bullet type)
        self.y_drag_coef = None  # drag coefficient of bullet in y dir (from bullet type)
        self.initial_speed = None  # initial speed of bullet (from bullet type)
        self.x_speed = None
        self.y_speed = None
        # set-up universal object properties
        self.gravity_dependent = True  # Is object is affected by gravity
        self.drag_dependent = True  # Is object is affected by air drag
        self.colision_dependent = True  # Is object collision cause it's destruction
        self.physics_circle_optimization = True  # Is object should use circle optimization,
        # not recommended for big objects

    def load_bullet(self, bullet_type, x_position=0, y_position=0):
        """
        method that will set up all bullet parameters
        :param bullet_type: string
        :param x_position: int
        :param y_position: int
        :return:
        """
        self.mass = self.bullets_config[bullet_type]['mass']
        self.x_drag_coef = self.bullets_config[bullet_type]['drag_coef']
        self.y_drag_coef = self.bullets_config[bullet_type]['drag_coef']
        self.initial_speed = self.bullets_config[bullet_type]['initial_speed']
        self.x_position = x_position
        self.y_position = y_position
        self.ref_point = Point(self.x_position, self.y_position)
        self.x_speed = 0
        self.y_speed = 0
        self.status = True  # status equal to True means that object isn't collide with any obstacles
        self.geometry = Geometry(self.ref_point, self.bullets_config[bullet_type]['geometry'])

    def shoot_bullet(self, shoot_angle):
        """
        Method that will start bullet movement
        """
        # angle of shoot in deg. 0 deg means shoot fully horizontally in +x dir
        self.x_speed = self.initial_speed * cos(radians(shoot_angle))
        # speed of bullet in x direction, initially equal to 0
        self.y_speed = self.initial_speed * sin(radians(shoot_angle))
        # speed of bullet in y direction, initially equal to 0

    def update_position(self, time_scale):
        """
        Method that will change position of object based on its speed
        :return:
        """
        self.x_position = self.x_position + time_scale * self.x_speed
        self.y_position = self.y_position + time_scale * self.y_speed
        self.ref_point = Point(self.x_position, self.y_position)

    def apply_gravity(self, time_scale, gravity):
        """
        Method that will apply gravity effects on object, changing its speed
        """
        self.y_speed = self.y_speed - time_scale * gravity

    def apply_drag(self, time_scale, wind_speed, density):
        """
        Method that will apply drag effects on object, changing its speed
        """
        x_drag_force = 0.5 * ((self.x_speed - wind_speed) ** 2)\
            * density * self.x_drag_coef * self.geometry.x_drag_surface
        x_drag_acc = x_drag_force / self.mass
        self.x_speed = self.x_speed - x_drag_acc * time_scale

        y_drag_force = 0.5 * (self.y_speed ** 2) * density * self.y_drag_coef * self.geometry.y_drag_surface
        y_drag_acc = y_drag_force / self.mass
        self.y_speed = self.y_speed - y_drag_acc * time_scale

    def simulate_time_step(self, time_scale=None, gravity=None,
                           wind_speed=None, density=None):
        self.update_position(time_scale)
        if self.gravity_dependent:
            self.apply_gravity(time_scale, gravity)
        if self.drag_dependent:
            self.apply_drag(time_scale, wind_speed, density)
        self.geometry.update(self.ref_point)


if __name__ == "__main__":
    test_time_scale = 0.001
    test_gravity = 9.8065
    test_wind_speed = -25
    test_density = 1.1
    test_time_steps = 6000
    test_angle = 45
    test_x_position = []
    test_y_position = []

    test_x_speed = []
    test_y_speed = []

    bullet = Bullet()
    test_bullet_type = 'Bullet1'
    bullet.load_bullet(test_bullet_type)
    bullet.shoot_bullet(test_angle)

    for _ in range(test_time_steps):
        if bullet.y_position < 0:
            break
        test_x_position.append(bullet.x_position)
        test_x_speed.append(bullet.x_speed)

        test_y_position.append(bullet.y_position)
        test_y_speed.append(bullet.y_speed)
        bullet.simulate_time_step(time_scale=test_time_scale, gravity=test_gravity,
                                  wind_speed=test_wind_speed, density=test_density)
    import matplotlib.pyplot as plt

    plt.plot(test_x_position, test_y_position)
    plt.show()
