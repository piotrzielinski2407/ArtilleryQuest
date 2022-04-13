import turtle
from bullet import Bullet
scale_factor = 0.1
screen_margin = 20
screen_size_width = 1600
screen_size_height = 900
screen_offset_horizontal = screen_margin - screen_size_width/2
screen_offset_vertical = screen_margin - screen_size_height/2


class GraphicDriver:
    def __init__(self, sim_env, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.buffer_objects = {}  # dict of objects to render
        self.buffer_texts = []  # list of text objects to write
        self.turtle_base = turtle
        self.turtle = self.turtle_base.Turtle()
        self.screen = self.turtle_base.Screen()
        self.barrel = None
        self.sim_env = sim_env
        self.screen.listen()
        self.__pre_sets()

    @property
    def sim_env(self):
        return self._sim_env

    @sim_env.setter
    def sim_env(self, new_value):
        self._sim_env = new_value
        if new_value is not None:
            self.screen.onkeypress(self.__prepare_and_shoot_bullet, "space")

    @property
    def barrel(self):
        return self._barrel

    @barrel.setter
    def barrel(self, new_value):
        self._barrel = new_value
        if new_value is not None:
            self.screen.onkeypress(self.barrel.decrease_angle, "q")
            self.screen.onkeypress(self.barrel.increase_angle, "e")

    def __pre_sets(self):
        self.turtle_base.setup(screen_size_width, screen_size_height)
        self.turtle.speed('fastest')
        self.turtle_base.tracer(n=0)
        self.turtle.hideturtle()
        self.turtle_base.listen()

    def update_screen(self, chunks_to_render, text_object_to_render=None):
        self.buffer_objects = self.__objects_buffer_update(chunks_to_render)
        self.buffer_texts = self.__texts_buffer_update(text_object_to_render)
        chunks_list = self.buffer_objects.values()
        text_objects = self.buffer_texts
        self.turtle.clear()
        for chunk in chunks_list:
            self.__render_chunk(chunk)
        for text_object in text_objects:
            self.__render_text(text_object)
        self.buffer_objects = self.__object_buffer_clean_up()
        self.buffer_texts = self.__texts_buffer_clean_up()
        self.turtle_base.update()

    def __prepare_and_shoot_bullet(self):
        angle = self.barrel.barrel_angle
        bullet_type = 'Bullet1'
        x_cord = self.barrel.barrel_end.x + self.barrel.ref_point.x
        y_cord = self.barrel.barrel_end.y + self.barrel.ref_point.y
        new_bullet = Bullet()
        new_bullet.load_bullet(angle, bullet_type, x_cord, y_cord)
        self.sim_env.add_object(new_bullet)
        new_bullet.shoot_bullet()
        self.sim_env.update_wind()

    def __object_buffer_clean_up(self):
        new_buffer = {}
        chunks_list = self.buffer_objects.values()
        for chunk in chunks_list:
            if chunk["status"] is False:
                if chunk["collision"] is True:
                    self.__make_explosion(chunk["geometry"])
            else:
                new_buffer.update({chunk["id"]: chunk})
        return new_buffer

    def __texts_buffer_clean_up(self):
        new_buffer = []
        for text_object in self.buffer_texts:
            if text_object.status is True:
                new_buffer.append(text_object)
        return new_buffer

    def __make_explosion(self, geometry):
        pass  # TODO will be implemented later

    @staticmethod
    def __objects_buffer_update(chunks_to_render):
        new_buffer = {}
        for single_chunk in chunks_to_render:
            new_buffer.update({single_chunk["id"]: single_chunk})
        return new_buffer

    @staticmethod
    def __texts_buffer_update(text_objects):
        if text_objects is not None:
            new_buffer = text_objects
        else:
            new_buffer = []
        return new_buffer

    def __render_chunk(self, chunk):
        self.turtle.pencolor(chunk["colors"]["boundary"])
        if chunk["fill"] is True:
            self.turtle.fillcolor(chunk["colors"]["fill"])
            self.turtle.begin_fill()

        self.__render_geometry(chunk["geometry"])
        if self.turtle.filling() is True:
            self.turtle.end_fill()

    def __render_geometry(self, geometry):
        lines_to_draw = geometry.geometry_boundaries
        for line in lines_to_draw:
            self.turtle.penup()
            self.turtle.goto(line.x1 + screen_offset_horizontal, line.y1 + screen_offset_vertical)
            self.turtle.pendown()
            self.turtle.goto(line.x2 + screen_offset_horizontal, line.y2 + screen_offset_vertical)
            self.turtle.penup()

    def __render_text(self, text_object):
        x = text_object.x_position
        y = text_object.y_position
        text = text_object.text
        align = text_object.align
        font = text_object.font
        color = text_object.color
        self.turtle.penup()
        self.turtle.goto(x + screen_offset_horizontal, y + screen_offset_vertical)
        self.turtle.color(color)
        self.turtle.pendown()
        self.turtle.write(text, align=align, font=font)
        self.turtle.penup()


if __name__ == "__main__":
    from graphic_object import UniversalGraphicObject
    from geometry import Geometry
    from point import Point
    import time

    boundary_color = 'red'
    line_thickness = 2
    fill_color = 'red'
    fill = True
    start_point = Point(0, 0)
    geometry_points = [[0, 0], [0, 50], [50, 50], [50, 0]]
    geometry_object = Geometry(start_point, geometry_points)
    graphic_object = UniversalGraphicObject()
    graphic_object.geometry = geometry_object
    graphic_object.boundary_color = boundary_color
    graphic_object.boundary_thickness = line_thickness
    graphic_object.fill_color = fill_color
    graphic_object.fill_object = True
    graphic_object.status = True
    graphic_object.explode_on_hit = True
    graphical_driver = GraphicDriver()

    for i in range(1, 20):
        chunks = [graphic_object.return_graphic_chunk()]
        graphical_driver.update_screen(chunks)
        ref_point = Point(i * 15, i * 15)
        time.sleep(0.017)
        graphic_object.geometry.update(ref_point)
    turtle.mainloop()
