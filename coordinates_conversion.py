import parameters
from math import sqrt


def convert_draw_coordinates(draw_coordinates):
    picture_coordinates_range = parameters.picture_br_corner[0] - parameters.picture_tl_corner[0]
    stretching_coefficient = parameters.window_height/picture_coordinates_range
    for i in range(len(draw_coordinates)):
        x_distance_from_tl_corner = draw_coordinates[i][0] - parameters.picture_tl_corner[0]
        y_distance_from_tl_corner = parameters.picture_tl_corner[1] - draw_coordinates[i][1]
        x_converted = stretching_coefficient*x_distance_from_tl_corner
        y_converted = stretching_coefficient*y_distance_from_tl_corner
        draw_coordinates[i] = (x_converted, y_converted)


def normalize_vector(vector, desired_norm):
    current_norm = sqrt(vector[0]**2 + vector[1]**2)
    if current_norm == 0:
        return vector
    normalized_x = vector[0]*desired_norm/current_norm
    normalized_y = vector[1]*desired_norm/current_norm
    return normalized_x, normalized_y

