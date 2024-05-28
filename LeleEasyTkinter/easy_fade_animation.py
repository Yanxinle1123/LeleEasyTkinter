import tkinter as tk

from LeleEasyTkinter.easy_auto_window import EasyAutoWindow
from LeleEasyTkinter.easy_button import EasyButton


def fade_in(window, alpha=0, ms=0):
    # 初始化窗口的透明度为0
    if alpha == 0:
        window.attributes('-alpha', 0)

    def start_fade_in_animation():
        nonlocal alpha
        if alpha >= 1:
            return
        alpha += 0.01
        window.attributes("-alpha", alpha)
        window.after(5, start_fade_in_animation)

    window.after(ms, start_fade_in_animation)


def fade_out(window, alpha=1, ms=0):
    def start_fade_out_animation():
        nonlocal alpha
        if alpha <= 0:
            window.destroy()
        else:
            alpha -= 0.01
            window.attributes("-alpha", alpha)
            window.after(5, start_fade_out_animation)

    window.after(ms, start_fade_out_animation)


if __name__ == '__main__':
    def quit_window():
        fade_out(root)


    root = tk.Tk()
    EasyAutoWindow(root, window_title="EasyAutoWindow", window_width_value=400, window_height_value=300, adjust_y=False,
                   adjust_x=False)
    EasyButton(root, "退出", expand=tk.YES, width=10, height=1, font_size=12, cmd=quit_window)
    root.after(500, fade_in(root, ms=500))
    root.mainloop()
