class EasyWindow:
    def __init__(self, window, window_title="window", adjust_x=True, adjust_y=True, minimum_value_x=20,
                 minimum_value_y=20,
                 maximum_value_x=4096, maximum_value_y=4096):
        self.window = window
        self.window_title = window_title
        self.adjust_x = adjust_x
        self.adjust_y = adjust_y
        self.minimum_value_x = minimum_value_x
        self.minimum_value_y = minimum_value_y
        self.maximum_value_x = maximum_value_x
        self.maximum_value_y = maximum_value_y

    def auto_position(self):
        # 获取屏幕的宽和高
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        # 获取窗口的宽和高
        window_width_value = screen_width - 100
        window_height_value = int(screen_height * 8.4) // 10

        # 计算窗口位置
        window_x_value = (screen_width - window_width_value) // 2
        window_y_value = (screen_height - window_height_value) // 2 - 20

        # 最终设置好位置
        self.window.geometry(f"{window_width_value}x{window_height_value}+{window_x_value}+{window_y_value}")
        self.window.title(self.window_title)
        self.window.resizable(self.adjust_x, self.adjust_y)
        self.window.minsize(self.minimum_value_x, self.minimum_value_y)
        self.window.maxsize(self.maximum_value_x, self.maximum_value_y)
