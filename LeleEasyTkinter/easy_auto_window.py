class EasyWindow:
    def __init__(self, window, window_title="window", adjust_x=True, adjust_y=True,
                 minimum_value_x=20,
                 minimum_value_y=20, maximum_value_x=4096, maximum_value_y=4096):
        self._window_y_value = None
        self._window_height_value = None
        self._screen_height = None
        self._window_width_value = None
        self._window_x_value = None
        self._screen_width = None
        self._window = window
        self._window_title = window_title
        self._adjust_x = adjust_x
        self._adjust_y = adjust_y
        self._minimum_value_x = minimum_value_x
        self._minimum_value_y = minimum_value_y
        self._maximum_value_x = maximum_value_x
        self._maximum_value_y = maximum_value_y

    def auto_position(self):
        # 获取屏幕的宽和高
        self._screen_width = self._window.winfo_screenwidth()
        self._screen_height = self._window.winfo_screenheight()

        # 获取窗口的宽和高
        self._window_width_value = self._screen_width - 100
        self._window_height_value = int(self._screen_height * 8.4) // 10

        # 计算窗口位置
        self._window_x_value = (self._screen_width - self._window_width_value) // 2
        self._window_y_value = (self._screen_height - self._window_height_value) // 2 - 20

        # 最终设置好位置
        self._window.geometry(
            f"{self._window_width_value}x{self._window_height_value}+{self._window_x_value}+{self._window_y_value}")
        self._window.title(self._window_title)
        self._window.resizable(self._adjust_x, self._adjust_y)
        self._window.minsize(self._minimum_value_x, self._minimum_value_y)
        self._window.maxsize(self._maximum_value_x, self._maximum_value_y)

    def get_window_width(self):
        return self._window.winfo_width()

    def get_window_height(self):
        return self._window.winfo_height()

    def get_window_x(self):
        return self._window_x_value

    def get_window_y(self):
        return self._window_y_value

    def get_window_title(self):
        return self._window_title
