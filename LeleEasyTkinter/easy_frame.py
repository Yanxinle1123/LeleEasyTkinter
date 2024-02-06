import tkinter


class EasyFrame:
    def __init__(self, window, side=tkinter.TOP, expand=False, fill=tkinter.NONE,
                 padx=0, pady=0, ipadx=0, ipady=0,
                 is_debug=False, text="",
                 font_size=17, width=17, height=0,
                 layout="pack", row=0, column=0, rowspan=1, columnspan=1):
        self._window = window
        self._text = text
        self._font_size = font_size
        self._width = width
        self._height = height
        self._is_debug = is_debug
        # self._bg = bg
        if self._is_debug:
            self._label_frame = tkinter.LabelFrame(window, text=self._text, font=("Arial", self._font_size),
                                                   height=self._height)

            if layout == "grid":
                self._label_frame.grid(row=row, column=column, rowspan=rowspan, columnspan=columnspan, sticky="nsew",
                                       padx=padx, pady=pady, ipadx=ipadx, ipady=ipady)
            else:
                self._label_frame.pack(side=side, expand=expand, fill=fill,
                                       padx=padx, pady=pady, ipadx=ipadx, ipady=ipady)
        else:
            self._frame = tkinter.Frame(window, height=self._height)

            if layout == "grid":
                self._frame.grid(row=row, column=column, rowspan=rowspan, columnspan=columnspan, sticky="nsew",
                                 padx=padx, pady=pady, ipadx=ipadx, ipady=ipady)
            else:
                self._frame.pack(side=side, expand=expand, fill=fill,
                                 padx=padx, pady=pady, ipadx=ipadx, ipady=ipady)

    def get_label_frame(self):
        return self._label_frame

    def get_frame(self):
        return self._frame

    def get(self):
        if self._is_debug:
            return self._label_frame
        else:
            return self._frame
