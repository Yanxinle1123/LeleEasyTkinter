import tkinter

from LeleEasyTkinter.easy_radio_button import EasyRadioButton

root = tkinter.Tk()
var = tkinter.IntVar()
var.set(2)  # 设置默认选项为第一个单选按钮
options = ["选项1", "选项2", "选项3", "选项4", "选项5", "选项6", "选项7"]
for i, option in enumerate(options, start=1):
    tkinter.Radiobutton(root, text=option, variable=var, value=i).pack()
EasyRadioButton(root, options, var)
root.mainloop()
