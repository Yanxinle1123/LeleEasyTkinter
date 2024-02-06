import tkinter
from tkinter import Label


class EasyLabel:
    def __init__(self, window, text, side=tkinter.TOP, expand=False, fill=tkinter.NONE,
                 padx=0, pady=0, ipadx=0, ipady=0, font_size=17,
                 layout="pack", row=0, column=0, rowspan=1, columnspan=1):
        self._window = window
        self._text = text
        self._font_size = font_size
        # self._bg = bg
        self._label = Label(window, text=self._text, font=("Arial", self._font_size))
        if layout == "grid":
            self._label.grid(row=row, column=column, rowspan=rowspan, columnspan=columnspan, sticky="nsew",
                             padx=padx, pady=pady, ipadx=ipadx, ipady=ipady)
        else:
            self._label.pack(side=side, expand=expand, fill=fill, padx=padx, pady=pady, ipadx=ipadx, ipady=ipady)

    def get_label(self):
        return self._label
