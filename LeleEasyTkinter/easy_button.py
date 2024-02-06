import tkinter

from tkinter import Button


class EasyButton:

    def __init__(self, window, text, cmd="", side=tkinter.TOP, expand=False, fill=tkinter.NONE,
                 padx=0, pady=0, ipadx=0, ipady=0, width=17, height=8, font_size=17,
                 layout="pack", row=0, column=0, rowspan=1, columnspan=1):
        self._window = window
        self._text = text
        self._command = cmd
        self._width = width
        self._height = height
        self._font_size = font_size
        self._button = Button(self._window, text=self._text, font=("Arial", self._font_size),
                              command=self._command, relief="raised", width=self._width,
                              height=self._height)
        if layout == "grid":
            self._button.grid(row=row, column=column, rowspan=rowspan, columnspan=columnspan, sticky="nsew",
                              padx=padx, pady=pady, ipadx=ipadx, ipady=ipady)
        else:
            self._button.pack(side=side, expand=expand, fill=fill, padx=padx, pady=pady, ipadx=ipadx, ipady=ipady)

    def get_button(self):
        return self._button
