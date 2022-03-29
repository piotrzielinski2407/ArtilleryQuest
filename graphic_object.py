from universal_object import UniversalObject


class UniversalGraphicObject(UniversalObject):
    def __init__(self, *args, **kwargs):
        # parent properties definition
        super().__init__(*args, **kwargs)
        self.id = self.id
        # that class properties definition
        self.boundary_color = None  # boundary color for graphic render
        self.boundary_thickness = None  # thickness of boundary line
        self.fill_color = None  # color to fill in
        self.fill_object = None  # if True, graphic render will fill created boundary with fill_color
        self.explode_on_hit = None  # if True, object will explode on collision (collision_dependent must be set True)

    def return_graphic_chunk(self):
        graphic_chunk = {
            "fill": self.fill_object,
            "thickness": self.boundary_thickness,
            "colors":
            {
                "boundary": self.boundary_color,
                "fill": self.fill_color
            },
            "geometry": self.geometry,
            "id": self.id,
            "status": self.status,
            "collision": self.explode_on_hit
        }

        return graphic_chunk

    def destruction_animation(self):
        pass  # TODO for future development
