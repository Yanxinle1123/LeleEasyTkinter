import tkinter

from LeleEasyTkinter.easy_auto_window import EasyAutoWindow
from LeleEasyTkinter.easy_button import EasyButton
from LeleEasyTkinter.easy_warning_windows import EasyWarningWindows


class EasyCheckButton:
    def __init__(self, window, text=None, set_=None, cmd=None, side=tkinter.TOP, expand=False, fill=tkinter.NONE,
                 padx=0, pady=0, ipadx=0, ipady=0, layout="pack", row=0, column=0, rowspan=1, columnspan=1):
        if text is None:
            text = ["选项1", "选项2", "选项3"]
        self._window = window
        self._text = text
        self._set = set_
        self._cmd = cmd
        self._vars = {}
        for options in self._text:
            var = tkinter.IntVar()
            check_button = tkinter.Checkbutton(self._window, text=options, variable=var)
            self._vars[options] = var
            if options in self._set:
                check_button.select()
            if layout == "grid":
                check_button.grid(row=row, column=column, rowspan=rowspan, columnspan=columnspan, sticky="nsew",
                                  padx=padx, pady=pady, ipadx=ipadx, ipady=ipady)
            else:
                check_button.pack(side=side, expand=expand, fill=fill, padx=padx, pady=pady, ipadx=ipadx,
                                  ipady=ipady)

    def get_set(self):
        selected_options = []
        for option, var in self._vars.items():
            if var.get() == 1:
                selected_options.append(option)
        return selected_options


if __name__ == "__main__":

    def get_set():
        fruit_set = fruit_check_button.get_set()
        if not fruit_set:
            fruit_set = "无选项"
        EasyWarningWindows("信息", fruit_set).show_warning()


    def quit_window():
        root.destroy()


    root = tkinter.Tk()
    EasyAutoWindow(root, window_title="CheckButton", window_width_value=500, window_height_value=500, adjust_x=False,
                   adjust_y=False)

    fruit_check_button = EasyCheckButton(root,
                                         text=["苹果(默认)", "香蕉(默认)", "橙子(默认)", "葡萄", "梨子(默认)", "榴莲",
                                               "荔枝", "草莓", "柚子", "樱桃", "杏子", "菠萝", "西瓜"],
                                         set_=["苹果(默认)", "梨子(默认)", "橙子(默认)", "香蕉(默认)"],
                                         expand=tkinter.YES)

    get_set_button = EasyButton(root, text="获取选项", font_size=12, width=6, height=1, cmd=get_set)

    quit_button = EasyButton(root, text="退出", font_size=12, width=6, height=1, cmd=quit_window)

    root.mainloop()
