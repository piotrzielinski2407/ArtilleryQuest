from wind import wind_gen
from itertools import combinations


class PhysicsSimulation:
    """
    Class that will conduct all physics calculations on objects
    1.Add objects to simulation
    2.Simulate time step
    3.Feed graphic render
    4.Clean-up
    """

    def __init__(self, timescale, gravity, air_density, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.timescale = timescale  # physical timescale, determined how often physical calculations should be conducted
        self.gravity = gravity  # gravity of planet, assumed constant during movement of projectile in [m/s2]
        self.air_density = air_density  # density of pressure, assumed constant during movement of projectile in [kg/m3]
        self.wind_object = wind_gen()  # to generator of wind speed
        self.wind_speed = self.wind_object.__next__()
        self.__objects = []

    def add_object(self, object_to_add):
        """
        Method that will add object to list of objects
        """
        self.__objects.append(object_to_add)

    def clean_up_objects(self):
        new_object_list = []
        for object_to_check in self.__objects:
            if object_to_check.status is True:
                new_object_list.append(object_to_check)
        return new_object_list

    def graphic_render_feed(self):
        chunks = []
        for object_to_render in self.__objects:
            chunks.append(object_to_render.return_graphic_chunk())
        return chunks

    def run_time_step(self):
        """
        Method that will simulate time-step
        """
        for physical_object in self.__objects:
            physical_object.simulate_time_step(self.timescale, self.gravity,
                                               self.wind_speed, self.air_density)
        self.check_collisions()

    def check_collisions(self):
        """
        Method to check collision between all objects
        """
        no_of_objects = len(self.__objects)
        check_sequence = list(combinations(list(range(no_of_objects)), 2))

        for sequence in check_sequence:
            object1 = self.__objects[sequence[0]]
            object2 = self.__objects[sequence[1]]
            collision_happen = self.check_objects_collision(object1, object2)
            if collision_happen is True:
                object1.collision_occur()
                object2.collision_occur()

    def check_objects_collision(self, object1, object2):
        """
        Method that will check if provided objects collide with each other
        :return: collision_happen
        """
        collision_happen = False  # By default, collision is considered as not happen
        for object1_boundary in object1.geometry.geometry_boundaries:

            for object2_boundary in object2.geometry.geometry_boundaries:
                collision_happen = self.check_boundary_collision(object1_boundary, object2_boundary)
                if collision_happen is True:
                    return collision_happen
        return collision_happen

    @staticmethod
    def check_boundary_collision(boundary1, boundary2):
        if boundary1.a is not None:
            if boundary2.a is not None:
                if boundary1.a != boundary2.a:
                    x_intersect = (boundary2.b-boundary1.b)/(boundary1.a-boundary2.a)
                    if (x_intersect >= boundary1.x1) and (x_intersect <= boundary1.x2):
                        return True
                    else:
                        return False
                else:
                    if boundary1.b == boundary2.b:
                        return True
                    else:
                        return False
            else:
                if (boundary2.x1 >= boundary1.x1) and (boundary2.x1 <= boundary1.x2):
                    return True
                else:
                    return False
        else:
            if boundary2.a is not None:
                if (boundary1.x1 >= boundary2.x1) and (boundary1.x1 <= boundary2.x2):
                    return True
                else:
                    return False
            else:
                if boundary1.x1 == boundary2.x1:
                    if (boundary1.y1 >= boundary2.y1) and (boundary1.y1 <= boundary2.y2):
                        return True
                    else:
                        return False
                else:
                    return False
