import tkinter


def on_submit():
    print("Selected value:", spinbox.get())


root = tkinter.Tk()
root.title("Spinbox Example")

# 创建 Spinbox
spinbox = tkinter.Spinbox(root, from_=1, to=10, state="readonly")
spinbox.pack()

# 创建一个提交按钮，单击时输出 Spinbox 的值
submit_button = tkinter.Button(root, text="Submit", command=on_submit)
submit_button.pack()

root.mainloop()
