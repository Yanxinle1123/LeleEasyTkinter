import tkinter as tk
import tkinter.messagebox as messagebox
from tkinter import simpledialog

from EasyTkinter.easy_auto_window import EasyAutoWindow


class EasyWarningWindows:
    def __init__(self, parent, title="警告", message="这是一个警告消息"):
        self._parent = parent
        self._title = title
        self._message = message

    def show_warning(self):
        if self._title == "警告":
            messagebox.showwarning(self._title, self._message, parent=self._parent)
        elif self._title == "信息":
            messagebox.showinfo(self._title, self._message, parent=self._parent)
        elif self._title == "错误":
            messagebox.showerror(self._title, self._message, parent=self._parent)
        elif self._title == "询问":
            result = messagebox.askquestion(self._title, self._message, parent=self._parent)
            return result
        elif self._title == "是/否":
            result = messagebox.askyesno(self._title, self._message, parent=self._parent)
            return result
        elif self._title == "输入框":
            result = simpledialog.askstring(self._title, self._message, parent=self._parent)
            return result

    def get_title(self):
        return self._title

    def get_message(self):
        return self._message


def demo_warning(root):
    EasyWarningWindows(root, "警告", "这是一个警告").show_warning()
    EasyWarningWindows(root, "信息", "这是一个信息").show_warning()
    EasyWarningWindows(root, "错误", "这是一个错误").show_warning()

    askquestion_result = EasyWarningWindows(root, "询问", "这是一条询问").show_warning()
    print(askquestion_result)

    askyesno_result = EasyWarningWindows(root, "是/否", "这是一个选择").show_warning()
    print(askyesno_result)

    askstring_result = EasyWarningWindows(root, "输入框", "这是一个输入框").show_warning()
    print(askstring_result)

    root.destroy()


if __name__ == '__main__':
    root = tk.Tk()
    EasyAutoWindow(root)
    root.attributes('-topmost', 'true')

    demo_warning(root)

    root.mainloop()
