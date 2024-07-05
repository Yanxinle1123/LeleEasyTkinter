import random
import tkinter

from LeleEasyTkinter.easy_auto_window import EasyAutoWindow
from LeleEasyTkinter.easy_button import EasyButton


def cubic_bezier(t, p0, p1, p2, p3):
    return (1 - t) ** 3 * p0 + 3 * (1 - t) ** 2 * t * p1 + 3 * (1 - t) * t ** 2 * p2 + t ** 3 * p3


def move_window_to(window, target_x, target_y, steps=200, amplitude=0.5):
    window.update_idletasks()

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    geometry = window.geometry().split('+')
    current_x = int(geometry[1])
    current_y = int(geometry[2])

    # 随机生成控制点，根据amplitude参数调整生成范围
    control_x1 = random.randint(int(current_x - amplitude * screen_width), int(current_x + amplitude * screen_width))
    control_y1 = random.randint(int(current_y - amplitude * screen_height), int(current_y + amplitude * screen_height))
    control_x2 = random.randint(int(target_x - amplitude * screen_width), int(target_x + amplitude * screen_width))
    control_y2 = random.randint(int(target_y - amplitude * screen_height), int(target_y + amplitude * screen_height))

    for i in range(steps + 1):
        t = i / steps

        x = int(cubic_bezier(t, current_x, control_x1, control_x2, target_x))
        y = int(cubic_bezier(t, current_y, control_y1, control_y2, target_y))

        window.geometry(f"+{x}+{y}")
        window.update()

    window.geometry(f"+{target_x}+{target_y}")


if __name__ == '__main__':
    root = tkinter.Tk()
    root.geometry("200x200")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    EasyAutoWindow(root, window_title="动画演示", window_width_value=210, window_height_value=100, adjust_x=False,
                   adjust_y=False)

    EasyButton(root, "移动窗口",
               cmd=lambda: move_window_to(root,
                                          target_x=random.randint(250, screen_width - 250),
                                          target_y=random.randint(250, screen_height - 250),
                                          steps=100,
                                          amplitude=0.2),
               width=10, height=1, font_size=12, expand=tkinter.YES)

    root.mainloop()
