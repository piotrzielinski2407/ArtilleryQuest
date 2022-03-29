import turtle
scale_factor = 0.1
screen_size_width = 1600
screen_size_height = 900


class GraphicDriver:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.buffer = {}  # list of objects to render
        self.turtle_base = turtle
        self.turtle = turtle.Turtle()
        self.screen = self.turtle.getscreen()
        self.__pre_sets()

    def __pre_sets(self):
        turtle.setup(screen_size_width, screen_size_height)
        self.turtle.speed('fastest')
        turtle.tracer(n=0)
        self.turtle.hideturtle()

    def update_screen(self, chunks_to_render):
        self.buffer = self.__buffer_update(chunks_to_render)
        chunks_list = self.buffer.values()
        self.turtle.clear()
        for chunk in chunks_list:
            self.__render_chunk(chunk)

        self.buffer = self.__buffer_clean_up()
        turtle.update()


    def __buffer_clean_up(self):
        new_buffer = {}
        chunks_list = self.buffer.values()
        for chunk in chunks_list:
            if chunk["status"] is False:
                if chunk["collision"] is True:
                    self.__make_explosion(chunk["geometry"])
            else:
                new_buffer.update({chunk["id"]: chunk})
        return new_buffer

    def __make_explosion(self, geometry):
        pass  # TODO will be implemented later

    @staticmethod
    def __buffer_update(chunks_to_render):
        new_buffer = {}
        for single_chunk in chunks_to_render:
            new_buffer.update({single_chunk["id"]: single_chunk})
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
            self.turtle.goto(line.x1, line.y1)
            self.turtle.pendown()
            self.turtle.goto(line.x2, line.y2)


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
