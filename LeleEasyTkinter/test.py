import math
import random
import tkinter


def move_window_to(window, target_x, target_y, steps=200):
    window.update_idletasks()
    geometry = window.geometry().split('+')
    current_x = int(geometry[1])
    current_y = int(geometry[2])

    distance_x = target_x - current_x
    distance_y = target_y - current_y

    for i in range(steps + 1):
        ratio = i / steps
        factor = 0.5 - 0.5 * math.cosh(ratio * math.pi)

        x = int(current_x + distance_x * factor)
        y = int(current_y + distance_y * factor)

        window.geometry(f"+{x}+{y}")
        window.update()

    window.geometry(f"+{target_x}+{target_y}")


def center_window(root):
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    move_window_to(root, x, y)


if __name__ == '__main__':
    root = tkinter.Tk()
    root.geometry("200x100")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    button = tkinter.Button(root, text="Move Window",
                            command=lambda: move_window_to(root,
                                                           random.randint(0, screen_width - 200),
                                                           random.randint(0, screen_height - 100)))
    button.pack(fill=tkinter.BOTH, expand=True)

    center_window(root)
    root.mainloop()
