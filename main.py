from tkinter import *
import useful_func
from axes import CoordinateAxes
import time
import parameters


root_window = Tk()
root_window.title('Phase space')
root_window.geometry('{}x{}'.format(parameters.window_width, parameters.window_height))

picture = Canvas(bg='white', width=parameters.window_height, height=parameters.window_height)
picture.pack(anchor='w')



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


    root_window.update()
    root_window.update_idletasks()

    frame_end = time.time()
    render_time = frame_end - frame_beginning
    if render_time < parameters.frame_time:
        time.sleep(parameters.frame_time - render_time)