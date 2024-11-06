from tkinter import *
from tkinter import ttk
import useful_func
from axes import CoordinateAxes
import time
import parameters


root_window = Tk()
root_window.title('Phase space')
root_window.geometry('{}x{}'.format(parameters.window_width, parameters.window_height))

picture = Canvas(bg='white', width=parameters.window_height, height=parameters.window_height)
picture.pack(anchor='w')


epsilon_label = ttk.Label(text='epsilon = {:.2f}'.format(useful_func.epsilon))
epsilon_scale = ttk.Scale(orient=VERTICAL, length=parameters.slider_length,
                          from_=parameters.epsilon_upper, to=parameters.epsilon_lower, value=useful_func.epsilon,
                          command=useful_func.update_epsilon)
epsilon_scale.place(x=parameters.window_height + parameters.slider_boarder_gap,
                    y=parameters.slider_boarder_gap)
epsilon_label.place(x=parameters.epsilon_label_x, y=useful_func.get_epsilon_label_y(), anchor='w')


c_label = ttk.Label(text='c = {:.2f}'.format(useful_func.c))
c_scale = ttk.Scale(orient=VERTICAL, length=parameters.slider_length, from_=parameters.c_upper, to=parameters.c_lower,
                          value=useful_func.c, command=useful_func.update_c)
c_scale.place(x=parameters.window_width - parameters.slider_boarder_gap, y=parameters.slider_boarder_gap, anchor='ne')
c_label.place(x=parameters.c_label_x, y=useful_func.get_c_label_y(), anchor='e')


phase_lines = useful_func.create_phase_lines(picture)


coordinate_axes = CoordinateAxes(tk_canvas=picture, x_lowest_value=parameters.picture_tl_corner[0],
                                 x_highest_value=parameters.picture_br_corner[0],
                                 y_lowest_value=parameters.picture_br_corner[1],
                                 y_highest_value=parameters.picture_tl_corner[1])
coordinate_axes.draw()


picture.bind('<MouseWheel>', useful_func.change_scale)


while True:
    frame_beginning = time.time()

    if useful_func.scale_change_occurred:
        useful_func.scale_change_occurred = False
        phase_lines = useful_func.update_phase_portrait(phase_lines)
        coordinate_axes.update_scale()

    if useful_func.parameter_change_occurred:
        useful_func.parameter_change_occurred = False
        epsilon_label['text'] = 'epsilon = {:.2f}'.format(useful_func.epsilon)
        epsilon_label.place(x=parameters.epsilon_label_x, y=useful_func.get_epsilon_label_y(), anchor='w')
        c_label['text'] = 'c = {:.2f}'.format(useful_func.c)
        c_label.place(x=parameters.c_label_x, y=useful_func.get_c_label_y(), anchor='e')
        phase_lines = useful_func.update_phase_portrait(phase_lines)
        coordinate_axes.update_scale()


    root_window.update()
    root_window.update_idletasks()

    frame_end = time.time()
    render_time = frame_end - frame_beginning
    if render_time < parameters.frame_time:
        time.sleep(parameters.frame_time - render_time)