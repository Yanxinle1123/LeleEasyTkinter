import tkinter

from LeleEasyTkinter.easy_auto_window import EasyAutoWindow


def center_window(root):
    width = root.winfo_width()
    height = root.winfo_height()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2 - 20

    root.focus_set()
    root.lift()
    root.geometry(f"+{x}+{y}")


def animate_resize_window(root, target_width, target_height, steps=100):
    # 获取当前窗口大小和位置
    geometry = root.geometry()
    current_width = int(geometry.split('x')[0])
    rest = geometry.split('x')[1].split('+')
    current_height = int(rest[0])
    current_x = int(rest[1])
    current_y = int(rest[2])

    # 计算每步的宽度和高度增量
    width_step = (target_width - current_width) / steps
    height_step = (target_height - current_height) / steps

    # 计算每步的位置增量
    x_step = width_step / 2
    y_step = height_step / 2

    # 逐步改变窗口大小和位置
    for i in range(steps):
        current_width += width_step
        current_height += height_step
        current_x -= x_step
        current_y -= y_step
        root.geometry(f"{int(current_width)}x{int(current_height)}+{int(current_x)}+{int(current_y)}")
        center_window(root)
        root.update()  # 更新窗口


root = tkinter.Tk()
EasyAutoWindow(root, window_title="动画演示", window_width_value=1, window_height_value=1, adjust_x=False,
               adjust_y=False)

animate_resize_window(root, 1000, 600)

root.mainloop()
