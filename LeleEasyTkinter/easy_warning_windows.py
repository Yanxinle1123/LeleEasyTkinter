import tkinter.messagebox as messagebox
from tkinter import simpledialog


class EasyWarningWindows:
    def __init__(self, title="警告", message="这是一个警告消息"):
        self._title = title
        self._message = message

    def show_warning(self):
        if self._title == "警告":
            messagebox.showwarning(self._title, self._message)
        elif self._title == "信息":
            messagebox.showinfo(self._title, self._message)
        elif self._title == "错误":
            messagebox.showerror(self._title, self._message)
        elif self._title == "询问":
            result = messagebox.askquestion(self._title, self._message)
            return result
        elif self._title == "是/否":
            result = messagebox.askyesno(self._title, self._message)
            return result
        elif self._title == "输入框":
            result = simpledialog.askstring(self._title, self._message)
            return result

    def get_title(self):
        return self._title

    def get_message(self):
        return self._message
