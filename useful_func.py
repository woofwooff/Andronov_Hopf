import parameters
from phase_line import PhaseLine


epsilon = 0.5
c = -2
scale_change_occurred = False


def dynamic_law1(x, y):
    dx = epsilon*x - y + c*x*(x**2 + y**2)
    dy = x + epsilon*y + c*y*(x**2 + y**2)
    return dx, dy


def change_scale(event):
    current_value_range = parameters.picture_br_corner[0] - parameters.picture_tl_corner[0]
    new_value_range = current_value_range*parameters.scale_change_factor**(-event.delta//120)
    if not new_value_range:
        new_value_range = 1e-16
    mouse_x_value = parameters.picture_tl_corner[0] + current_value_range*(event.x/parameters.window_height)
    mouse_y_value = parameters.picture_tl_corner[1] - current_value_range*(event.y/parameters.window_height)
    new_tl_corner = (mouse_x_value - new_value_range*0.5, mouse_y_value + new_value_range*0.5)
    new_br_corner = (mouse_x_value + new_value_range*0.5, mouse_y_value - new_value_range*0.5)
    parameters.picture_tl_corner = new_tl_corner
    parameters.picture_br_corner = new_br_corner
    global scale_change_occurred
    scale_change_occurred = True



def generate_phase_space_grid():
    starting_points = []
    picture_value_range = parameters.picture_br_corner[0] - parameters.picture_tl_corner[0]
    for i in range(parameters.phase_line_density):
        for j in range(parameters.phase_line_density):
            point_x = (parameters.picture_tl_corner[0] +
                       (1 + i)*picture_value_range*(1/(parameters.phase_line_density+1)))
            point_y = (parameters.picture_tl_corner[1] -
                       (1 + j)*picture_value_range*(1/(parameters.phase_line_density + 1)))
            starting_points.append((point_x, point_y))
    return starting_points


def generate_phase_space_circle():
    pass


def create_phase_lines(tk_canvas):
    starting_points = generate_phase_space_grid()
    phase_lines = []
    for point in starting_points:
        phase_line = PhaseLine(starting_coordinates=point, evolution_function=dynamic_law1,
                               tk_canvas=tk_canvas)
        phase_lines.append(phase_line)
        phase_line.draw()
    return phase_lines


def update_phase_portrait(phase_lines):
    canvas = phase_lines[0].canvas
    for line in phase_lines:
        line.canvas.delete(line.image_forward)
        line.canvas.delete(line.image_backward)
    new_phase_lines = create_phase_lines(canvas)
    return new_phase_lines

