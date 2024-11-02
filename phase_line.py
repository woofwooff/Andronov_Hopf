import parameters
import tkinter as tk
from coordinates_conversion import normalize_vector, convert_draw_coordinates


class PhaseLine:

    def __init__(self, starting_coordinates, evolution_function, tk_canvas):
        self.function = evolution_function
        self.canvas = tk_canvas
        self.beginning = starting_coordinates
        self.iteration_step = ((parameters.picture_br_corner[0] -
                                parameters.picture_tl_corner[0])*parameters.iteration_step_precision)
        self.forward_coordinates = [starting_coordinates]
        self.backward_coordinates = [starting_coordinates]
        self.image_forward = None
        self.image_backward = None

    def draw(self):
        self.iterate()
        backward_draw_coordinates = self.backward_coordinates[::-1]
        convert_draw_coordinates(backward_draw_coordinates)
        self.image_backward = self.canvas.create_line(backward_draw_coordinates, fill=parameters.phase_line_color,
                                                      arrow=tk.LAST)
        forward_draw_coordinates = self.forward_coordinates
        convert_draw_coordinates(forward_draw_coordinates)
        self.image_forward = self.canvas.create_line(forward_draw_coordinates, fill=parameters.phase_line_color)

    def one_iteration_forward(self):
        point = self.forward_coordinates[-1]
        dx, dy = self.function(point[0], point[1])
        normalized_vector = normalize_vector((dx, dy), self.iteration_step)
        next_point = (point[0] + normalized_vector[0], point[1] + normalized_vector[1])
        self.forward_coordinates.append(next_point)

    def one_iteration_backwards(self):
        point = self.backward_coordinates[-1]
        dx, dy = self.function(point[0], point[1])
        normalized_vector = normalize_vector((dx, dy), self.iteration_step)
        previous_point = (point[0] - normalized_vector[0], point[1] - normalized_vector[1])
        self.backward_coordinates.append(previous_point)

    def iterate(self):
        for i in range(parameters.max_number_of_iterations):
            self.one_iteration_forward()
            self.one_iteration_backwards()
