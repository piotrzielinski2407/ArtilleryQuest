from unittest import TestCase
terrain_geometry1 = [[0, 0], [80, 0], [160, 200], [250, 0], [450, 0]]


class TestTerrain(TestCase):
    def test_set_up_terrain(self):
        from unittest.mock import mock_open, patch
        import json
        variant = "variant1"
        read_data = json.dumps({"geometry": {variant: terrain_geometry1}})
        mock_open = mock_open(read_data=read_data)
        with patch('builtins.open', mock_open):
            from terrain import Terrain
            test_terrain_object = Terrain()
            test_terrain_object.set_up_terrain(variant)
            self.assertTrue(test_terrain_object.status is True)
            self.assertTrue(test_terrain_object.ref_point.x == 0)
            self.assertTrue(test_terrain_object.ref_point.y == 0)
            index = 0
            for cords_pair in terrain_geometry1:
                self.assertTrue(test_terrain_object.geometry.geometry_points[index].x == cords_pair[0])
                self.assertTrue(test_terrain_object.geometry.geometry_points[index].y == cords_pair[1])
                index += 1

