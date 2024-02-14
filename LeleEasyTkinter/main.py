import tkinter

from LeleEasyTkinter.easy_auto_window import EasyWindow
from LeleEasyTkinter.easy_button import EasyButton
from LeleEasyTkinter.easy_drop_list import EasyDropList
from LeleEasyTkinter.easy_frame import EasyFrame
from LeleEasyTkinter.easy_label import EasyLabel
from LeleEasyTkinter.easy_multi_text import EasyMultiText
from LeleEasyTkinter.easy_radio_button import EasyRadioButton
from LeleEasyTkinter.easy_warning_windows import EasyWarningWindows


def on_select():
    #
    pass


def layout_by_pack(win):
    warning_windows = EasyWarningWindows(title="信息",
                                         message="欢迎使用中英文翻译程序\nWelcome to the Chinese and English translation program")
    warning_windows.show_warning()

    # 增加label
    f1 = EasyFrame(win, tkinter.TOP, True, tkinter.BOTH, pady=2).get()

    f11 = EasyFrame(f1, tkinter.LEFT, True, tkinter.BOTH, padx=2).get()

    f111 = EasyFrame(f11, tkinter.TOP, True, tkinter.BOTH).get()
    translate_label_need = EasyLabel(f111, "需要翻译的文本：", tkinter.LEFT)
    translate_text_need = EasyMultiText(f111, tkinter.LEFT, True, tkinter.BOTH)

    f112 = EasyFrame(f11, tkinter.TOP, True, tkinter.BOTH).get()
    translate_label_after = EasyLabel(f112, "翻译之后的文本：", tkinter.LEFT)
    translate_text_after = EasyMultiText(f112, tkinter.LEFT, True, tkinter.BOTH, state_str="disabled")

    f12 = EasyFrame(f1, tkinter.LEFT, False, tkinter.Y, padx=2).get()
    translate_label = EasyLabel(f12, "翻译语言码：", tkinter.TOP, True, tkinter.BOTH)
    translate_en_button = EasyDropList(f12,
                                       ["英语(en)", "中文简体(zh-CN)", "中文繁体(zh-TW)", "西班牙语(es)",
                                        "法语(fr)", "德语(de)", "日语(ja)", "韩语(ko)", "俄语(ru)",
                                        "葡萄牙语(pt)", "意大利语(it)", "荷兰语(nl)", "瑞典语(sv)",
                                        "波兰语(pl)", "丹麦语(da)", "希腊语(el)", "芬兰语(fi)",
                                        "捷克语(cs)", "匈牙利语(hu)", "挪威语(no)", "泰语(th)",
                                        "印度尼西亚语(id)", "越南语(vi)", "马来语(ms)", "土耳其语(tr)"],
                                       on_select, tkinter.TOP, True,
                                       tkinter.X)
    translate_cn_button = EasyButton(f12, "翻译", None,
                                     tkinter.TOP, True, tkinter.BOTH)

    f13 = EasyFrame(f1, tkinter.LEFT, False, tkinter.Y).get()
    translate_auto_radio_button = EasyRadioButton(f13, ["自动翻译关", "自动翻译开"], tkinter.NONE,
                                                  expand=True,
                                                  fill=tkinter.Y)

    f2 = EasyFrame(win, tkinter.TOP, False, tkinter.X, pady=2).get()
    quit_button = EasyButton(f2, "退出",
                             quit, tkinter.TOP, False, tkinter.BOTH,
                             padx=2, height=2)


window = tkinter.Tk()

easy_window = EasyWindow(window, "测试窗口")
a, b = easy_window.auto_position()
layout_by_pack(window)
print(a, b)
window.mainloop()
