import tkinter as tk

from easy_auto_window import EasyAutoWindow
from easy_button import EasyButton


def fade_in(window, alpha=0):
    if alpha >= 1:
        return
    window.attributes("-alpha", alpha)
    window.after(5, fade_in, window, alpha + 0.01)


def fade_out(window, alpha=1):
    if alpha <= 0:
        window.destroy()
    else:
        window.attributes("-alpha", alpha)
        window.after(5, fade_out, window, alpha - 0.01)


if __name__ == '__main__':
    def quit_window():
        fade_out(root)


    root = tk.Tk()
    EasyAutoWindow(root, window_title="EasyAutoWindow", window_width_value=400, window_height_value=300, adjust_y=False,
                   adjust_x=False)
    EasyButton(root, "退出", expand=tk.YES, width=10, height=1, font_size=12, cmd=quit_window)
    root.after(500, fade_in(root))
    root.mainloop()
