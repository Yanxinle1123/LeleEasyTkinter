import tkinter

from LeleEasyTkinter.easy_auto_window import EasyAutoWindow
from LeleEasyTkinter.easy_button import EasyButton

root = tkinter.Tk()
EasyAutoWindow(root, window_title="Button", window_width_value=150, window_height_value=80, adjust_x=True,
               adjust_y=True)

EasyButton(root, "Button", expand=tkinter.YES, fill=tkinter.BOTH, auto_resize_font=True)

root.mainloop()
