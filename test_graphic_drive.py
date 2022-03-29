from unittest import TestCase
from graphic_object import UniversalGraphicObject
from geometry import Geometry
from point import Point
from graphic_drive import GraphicDriver
import time
boundary_color = 'red'
line_thickness = 2
fill_color = 'red'
fill = True


class TestGraphicDriver(TestCase):
    def test_update_screen(self):
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

        for i in range(1, 30):
            chunks_to_render = [graphic_object.return_graphic_chunk()]
            graphical_driver.update_screen(chunks_to_render)
            ref_point = Point(i*15, i*15)
            time.sleep(0.017)
            graphic_object.geometry.update(ref_point)
