import parameters


class CoordinateAxes:

    def __init__(self, tk_canvas, x_lowest_value, x_highest_value, y_lowest_value, y_highest_value):
        self.canvas = tk_canvas
        self.x_lowest = x_lowest_value
        self.x_highest = x_highest_value
        self.y_lowest = y_lowest_value
        self.y_highest = y_highest_value
        self.x_axis = None
        self.y_axis = None
        self.x_marks = []
        self.y_marks = []
        self.mark_pictures = []
        self.mark_backgrounds = []

    def draw(self):
        self.draw_axes()
        self.draw_axes_marks()
        self.draw_mark_numbers()
        self.draw_numbers_background()

    def draw_axes(self):
        x_axis_beginning = (parameters.axes_boarder_gap * 2 - 1,
                            parameters.window_height - parameters.axes_boarder_gap)
        x_axis_end = (parameters.window_height - parameters.axes_boarder_gap * 2 + 1,
                      parameters.window_height - parameters.axes_boarder_gap)
        self.x_axis = self.canvas.create_line(x_axis_beginning, x_axis_end, fill=parameters.axes_color,
                                              width=parameters.axes_thickness)
        y_axis_beginning = (parameters.axes_boarder_gap,
                            parameters.window_height - parameters.axes_boarder_gap * 2 + 1)
        y_axis_end = (parameters.axes_boarder_gap, parameters.axes_boarder_gap * 2 - 1)
        self.y_axis = self.canvas.create_line(y_axis_beginning, y_axis_end, fill=parameters.axes_color,
                                              width=parameters.axes_thickness)

    def draw_axes_marks(self):
        axis_length = parameters.window_height - 4*parameters.axes_boarder_gap
        for i in range(parameters.axes_mark_number):
            x_mark_beginning = (2*parameters.axes_boarder_gap + axis_length*i/(parameters.axes_mark_number - 1),
                                parameters.window_height - parameters.axes_boarder_gap)
            x_mark_end = (2*parameters.axes_boarder_gap + axis_length*i/(parameters.axes_mark_number - 1),
                                parameters.window_height - parameters.axes_boarder_gap + parameters.axes_mark_length)
            x_mark = self.canvas.create_line(x_mark_beginning, x_mark_end, fill=parameters.axes_color,
                                             width=parameters.axes_marks_thickness)
            self.x_marks.append(x_mark)
            y_mark_beginning = (parameters.axes_boarder_gap, parameters.window_height - parameters.axes_boarder_gap*2 -
                                axis_length*i/(parameters.axes_mark_number - 1))
            y_mark_end = (parameters.axes_boarder_gap - parameters.axes_mark_length,
                          parameters.window_height - parameters.axes_boarder_gap*2 -
                          axis_length*i/(parameters.axes_mark_number - 1))
            y_mark = self.canvas.create_line(y_mark_beginning, y_mark_end, fill=parameters.axes_color,
                                             width=parameters.axes_marks_thickness)
            self.x_marks.append(y_mark)

    def draw_mark_numbers(self):
        axis_length = parameters.window_height - 4 * parameters.axes_boarder_gap
        picture_values_range = parameters.picture_br_corner[0] - parameters.picture_tl_corner[0]
        upscale_coeff = picture_values_range/parameters.window_height
        for i in range(parameters.axes_mark_number):
            x_mark_value = (parameters.picture_tl_corner[0] + 2*parameters.axes_boarder_gap*upscale_coeff +
                            axis_length*i/(parameters.axes_mark_number - 1)*upscale_coeff)
            x_mark_text = '{:.1e}'.format(x_mark_value)
            x_mark_position = (2*parameters.axes_boarder_gap + axis_length*i/(parameters.axes_mark_number - 1),
                                parameters.window_height - parameters.axes_boarder_gap + parameters.axes_mark_length +
                               parameters.axes_mark_numbers_offset)
            x_mark_picture = self.canvas.create_text(x_mark_position, text=x_mark_text, fill=parameters.axes_mark_color,
                                    font=parameters.axes_mark_numbers_font, anchor='n')
            self.mark_pictures.append(x_mark_picture)
            y_mark_value = (parameters.picture_br_corner[1] + 2 * parameters.axes_boarder_gap * upscale_coeff +
                            axis_length * i / (parameters.axes_mark_number - 1) * upscale_coeff)
            y_mark_text = '{:.1e}'.format(y_mark_value)
            y_mark_position = (parameters.axes_boarder_gap - parameters.axes_mark_length -
                               parameters.axes_mark_numbers_offset,
                               parameters.window_height - parameters.axes_boarder_gap*2 -
                          axis_length*i/(parameters.axes_mark_number - 1))
            y_mark_picture = self.canvas.create_text(y_mark_position, text=y_mark_text, fill=parameters.axes_mark_color,
                                    font=parameters.axes_mark_numbers_font, anchor='e')
            self.mark_pictures.append(y_mark_picture)

    def draw_numbers_background(self):
        for picture in self.mark_pictures:
            background_rectangle = self.canvas.create_rectangle(self.canvas.bbox(picture), fill='white',
                                                                outline='white')
            self.canvas.tag_raise(picture)
            self.mark_backgrounds.append(background_rectangle)

    def update_scale(self):
        for picture in self.mark_pictures:
            self.canvas.delete(picture)
        self.mark_pictures = []
        for background in self.mark_backgrounds:
            self.canvas.delete(background)
        self.mark_backgrounds = []
        self.draw_mark_numbers()
        self.draw_numbers_background()
