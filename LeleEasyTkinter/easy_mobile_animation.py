import math
import random
import tkinter

from LeleEasyTkinter.easy_auto_window import EasyAutoWindow
from LeleEasyTkinter.easy_button import EasyButton


def move_window_to(window, target_x, target_y, steps=100):
    # 获取当前窗口的位置和大小
    geometry = window.geometry().split('+')
    current_x = int(geometry[1])
    current_y = int(geometry[2])

    # 计算需要移动的距离
    distance_x = target_x - current_x
    distance_y = target_y - current_y

    # 逐像素移动窗口
    for i in range(steps + 1):
        ratio = i / steps
        factor = 0.5 - 0.5 * math.cos(ratio * math.pi)  # 使用正弦函数计算移动因子

        x = int(current_x + distance_x * factor)
        y = int(current_y + distance_y * factor)

        window.geometry(f"+{x}+{y}")
        window.update()

    # 确保窗口移动到准确的目标位置
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
                                          steps=100),
               width=10, height=1, font_size=12, expand=tkinter.YES)

    root.mainloop()
