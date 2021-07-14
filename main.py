
import tkinter as tk

# 一つ前のボタン情報を格納する変数
previousBtnText = None

# button一覧
buttonList = [
    '7',
    '8',
    '9',
    'C',
    '4',
    '5',
    '6',
    '+',
    '1',
    '2',
    '3',
    '-',
    '0',
    '=',
]

# buttonの選択により、label Widgetの値を変更する。
def showDisplay(event):
    global previousBtnText

    # buttonの選択内容
    btnText = event.widget['text']
    # 現在label Widgetへ描画されるテキスト情報
    currentText = sv.get()

    if btnText == 'C' or (btnText in ('+', '-', '=') and currentText == ''):
        sv.set('')
        previousBtnText = None
    elif previousBtnText in ('+', '-'):
        previousBtnText = btnText
    elif btnText == '=':
        if not currentText[len(currentText) - 1] in ('+', '-'):
            ans = eval(currentText)
            if ans == 0:
                sv.set('')
            else:
                sv.set(ans)
            previousBtnText = btnText
    else:
        sv.set(currentText + btnText)
        previousBtnText = btnText

# Windowを作成する。
root = tk.Tk()

# Windowを親要素として、frame Widget(Frame)を作成する。
# Frameについて : https://kuroro.blog/python/P20XOidA5nh583fYRvxf/
f = tk.Frame(root)

# Windowを親要素として、frame Widget(Frame)をどのように配置するのか?
# gridについて : https://kuroro.blog/python/JoaowDiUdLAOj3cSBxiX/
f.grid()

row = 1
column = 0
for button in buttonList:
    # frame Widget(Frame)を親要素として、button Widgetを作成する。
    # text : テキスト情報
    # width : 幅の設定
    # Buttonについて : https://kuroro.blog/python/oFju6EngDtcYtIiMIDf1/
    btn = tk.Button(f, text=button, width=2)

    if button == 'C':
        btn.configure(highlightbackground='#ff0000')
    if button in ('+', '-', '='):
        btn.configure(highlightbackground='#00ff00')

    # frame Widget(Frame)を親要素として、button Widgetをどのように配置するのか?
    # gridについて : https://kuroro.blog/python/JoaowDiUdLAOj3cSBxiX/
    btn.grid(row=row, column=column)
    # ボタンを選択した場合に実行する関数を設定する。
    # bindについて : https://kuroro.blog/python/eI5ApJE1wkU7bHsuwk0H/
    btn.bind("<1>", showDisplay)

    if column == 3:
        column = 0
        row = row + 1
    else:
        column = column + 1

    # = buttonを配置するための位置調整
    if row == 4 and column == 1:
        column = 3

# label Widgetの文字列情報をstring型の変数とする。
# StringVarについて : https://kuroro.blog/python/K53voPjJuKFfYrjmP8FP/
sv = tk.StringVar()
# label Widgetの文字列情報の初期化を行う。
sv.set('')

# frame Widget(Frame)を親要素として、label Widgetを作成する。
# textvariable : label Widgetへ文字列を表示する。値を可変なsvとする。
# Labelについて : https://kuroro.blog/python/Pj4Z7JBNRvcHZvtFqiKD/
label = tk.Label(f, textvariable=sv)
# frame Widget(Frame)を親要素として、label Widgetをどのように配置するのか?
# gridについて : https://kuroro.blog/python/JoaowDiUdLAOj3cSBxiX/
label.grid(row=0, column=0, columnspan=4)

# Windowをループさせて、継続的にWindow表示させる。
# mainloopについて : https://kuroro.blog/python/DmJdUb50oAhmBteRa4fi/
root.mainloop()
