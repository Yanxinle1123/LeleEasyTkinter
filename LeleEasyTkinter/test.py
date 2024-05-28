import tkinter as tk

from easy_fade_animation import fade_in, fade_out

root = tk.Tk()
root.geometry("300x200")

fade_in(root)

button = tk.Button(root, text="点击淡出", command=lambda: fade_out(root))
button.pack()

root.mainloop()
