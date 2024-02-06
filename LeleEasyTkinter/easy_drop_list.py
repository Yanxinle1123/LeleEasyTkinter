import tkinter


class EasyDropList:

    def __init__(self, window, options=None, cmd=None, side=tkinter.TOP, expand=False,
                 fill=tkinter.NONE, padx=0, pady=0, ipadx=0, ipady=0, width=17, height=8, font_size=17,
                 layout="pack", row=0, column=0, rowspan=1, columnspan=1):
        if options is None:
            options = ['选项1', '选项2', '选项3']
        self._window = window
        self._options = options
        self._command = cmd
        self._width = width
        self._height = height
        self._font_size = font_size

        self._selected_option = tkinter.StringVar(self._window)
        self._selected_option.set(self._options[0])  # 默认选中第一个选项
        self._combo = tkinter.OptionMenu(self._window, self._selected_option, *self._options)
        if layout == "grid":
            self._combo.grid(row=row, column=column, rowspan=rowspan, columnspan=columnspan, sticky="nsew",
                             padx=padx, pady=pady, ipadx=ipadx, ipady=ipady)
        else:
            self._combo.pack(side=side, expand=expand, fill=fill, padx=padx, pady=pady, ipadx=ipadx, ipady=ipady)

    def get_combo(self):
        return self._combo

    def get_combo_value(self):
        return self._selected_option.get()
