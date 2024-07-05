import math
import random
import tkinter

from LeleEasyTkinter.easy_button import EasyButton


def move_window_to(window, target_x, target_y, step=1):
    # 获取当前窗口的位置和大小
    geometry = window.geometry().split('+')
    current_x = int(geometry[1])
    current_y = int(geometry[2])

    # 计算需要移动的距离
    distance_x = target_x - current_x
    distance_y = target_y - current_y

    # 计算总距离和每一步的距离
    total_distance = math.sqrt(distance_x ** 2 + distance_y ** 2)
    steps = int(total_distance / step)

    # 如果 steps 为 0，直接将窗口移动到目标位置并返回
    if steps == 0:
        window.geometry(f"+{target_x}+{target_y}")
        return

    # 计算每一步的 x 和 y 方向上的距离
    step_x = distance_x / steps
    step_y = distance_y / steps

    # 逐像素移动窗口
    for _ in range(steps):
        current_x += step_x
        current_y += step_y
        window.geometry(f"+{int(current_x)}+{int(current_y)}")
        window.update()

    # 确保窗口移动到准确的目标位置
    window.geometry(f"+{target_x}+{target_y}")


if __name__ == '__main__':
    root = tkinter.Tk()
    root.geometry("200x200")
    root.resizable(False, False)

    # 获取屏幕的大小
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # 创建一个按钮，点击时将窗口移动到屏幕内的一个随机位置
    EasyButton(root, "移动窗口",
               cmd=lambda: move_window_to(root,
                                          target_x=random.randint(0, screen_width - 500),
                                          target_y=random.randint(0, screen_height - 500),
                                          step=20),
               width=10, height=1, font_size=12, expand=tkinter.YES)

    root.mainloop()
