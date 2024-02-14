import tkinter

from LeleEasyTkinter.easy_radio_button import EasyRadioButton

root = tkinter.Tk()
var = tkinter.IntVar()
var.set(2)
options = ["选项1", "选项2", "选项3", "选项4", "选项5", "选项6", "选项7"]
EasyRadioButton(root, options, var, )
root.mainloop()
