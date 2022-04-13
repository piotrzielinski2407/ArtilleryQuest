class TextObject:
    def __init__(self, x_position, y_position, status=True, text="", align='left', color='black', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.x_position = x_position
        self.y_position = y_position
        self.status = status  # status equal to True means that object should persist for next render
        self.text = text
        self.align = align
        self.font = ('Arial', 30, 'normal')  # this is default font
        self.color = color

    def update_text(self, new_text):
        self.text = new_text


if __name__ == '__main__':
    test_object = TextObject(100, 200)
    test_object.update_text('some text')
