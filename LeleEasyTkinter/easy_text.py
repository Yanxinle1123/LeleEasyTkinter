import tkinter
from tkinter import Entry


class EasyText:
    def __init__(self, win, side=tkinter.TOP, expand=False, fill=tkinter.NONE,
                 padx=0, pady=0, ipadx=0, ipady=0, width=30, font_size=17, state_str="normal",
                 layout="pack", row=0, column=0, rowspan=1, columnspan=1):
        self._win = win
        self._width = width
        self._font_size = font_size
        self._state_str = state_str
        self._entry = Entry(win, font=("Aria", self._font_size), width=self._width, state=self._state_str)
        if layout == "grid":
            self._entry.grid(row=row, column=column, rowspan=rowspan, columnspan=columnspan, sticky="nsew",
                             padx=padx, pady=pady, ipadx=ipadx, ipady=ipady)
        else:
            self._entry.pack(side=side, expand=expand, fill=fill, padx=padx, pady=pady, ipadx=ipadx, ipady=ipady)

    def get_text(self):
        return self._entry
