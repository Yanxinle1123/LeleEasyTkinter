import tkinter


class EasyRadioButton:
    def __init__(self, window, text=['选项1', '选项2'], cmd=None, side=tkinter.TOP, expand=False,
                 fill=tkinter.NONE, padx=0, pady=0, ipadx=0, ipady=0, width=17, height=8, font_size=17,
                 layout="pack", row=0, column=0, rowspan=1, columnspan=1):
        self._window = window
        self._options1 = text[0]
        self._options2 = text[1]
        self._command = cmd
        self._width = width
        self._height = height
        self._font_size = font_size

        self._var = tkinter.IntVar()
        self._var.set(2)
        self._radio_button1 = tkinter.Radiobutton(self._window, text=self._options1, variable=self._var, value=1)
        self._radio_button2 = tkinter.Radiobutton(self._window, text=self._options2, variable=self._var, value=2)

        if layout == "grid":
            self._radio_button1.grid(row=row, column=column, rowspan=rowspan, columnspan=columnspan, sticky="nsew",
                                     padx=padx, pady=pady, ipadx=ipadx, ipady=ipady)
            self._radio_button2.grid(row=row, column=column, rowspan=rowspan, columnspan=columnspan, sticky="nsew",
                                     padx=padx, pady=pady, ipadx=ipadx, ipady=ipady)
        else:
            self._radio_button1.pack(side=side, expand=expand, fill=fill, padx=padx, pady=pady, ipadx=ipadx,
                                     ipady=ipady)
            self._radio_button2.pack(side=side, expand=expand, fill=fill, padx=padx, pady=pady, ipadx=ipadx,
                                     ipady=ipady)

    def get_radio_button(self):
        return self._radio_button1, self._radio_button2

    def get_radio_button_value(self):
        return self._var.get()
