from unittest import TestCase
wind_range = 25
test_loops = 1000


class Test(TestCase):
    def test_wind_gen(self):
        from unittest.mock import mock_open, patch
        import json
        read_data = json.dumps({"wind_boundaries": wind_range})
        mock_open = mock_open(read_data=read_data)
        with patch('builtins.open', mock_open):
            from wind import wind_gen
            for _ in range(test_loops):
                wind = wind_gen().__next__()
                self.assertTrue(isinstance(wind, float))
                self.assertGreater(wind, -wind_range)
