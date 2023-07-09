import tkinter as tk
import time

app = tk.Tk()
app.wm_attributes('-topmost',1)

TOTAL_TIME = 5
second = TOTAL_TIME
is_running = False

def time_to_string(s):
    """
    秒数转化成时间格式
    :param s: second
    :return: str
    """
    return time.strftime("%H时%M分%S秒", time.gmtime(s))


def click_start_button():
    """点击后开始倒计时，页面每秒刷新一次"""
    global is_running
    if is_running:
        # 停止倒计时
        start_button.config(text="开始")
        is_running = False
    else:
        # 开始倒计时
        start_button.config(text="暂停")
        is_running = True
        update_time()


def click_reset_button():
    global is_running, second
    if not is_running:
        start_button.config(text="开始")
        is_running = False
        second = TOTAL_TIME
        dstr.set(time_to_string(second))


def update_time():
    """
    更新时间
    :return:
    """
    global second, is_running
    # 倒计时完成停止运行
    if second <= 0:
        is_running = False
        dstr.set(time_to_string(0))
        start_button.config(text="开始")
    # 每秒倒计时并刷新时间
    if is_running:
        second -= 1
        dstr.set(time_to_string(second))
        app.after(1000, update_time)

menubar = tk.Menu(app)
menubar.add_command(label='设置', command=None)
app.config(menu=menubar)

dstr = tk.StringVar()
dstr.set(time_to_string(second))
time_label = tk.Label(app, textvariable=dstr, font=('Arial', 30))
time_label.grid(row=0, column=0, pady=10, columnspan=2)

start_button = tk.Button(app, text="开始", font=('Arial', 18), width=10, height=1)
start_button.grid(row=1, column=0, padx=10, pady=10)
start_button.config(command=click_start_button)

reset_button = tk.Button(app, text="重置", font=('Arial', 18), width=10, height=1)
reset_button.grid(row=1, column=1, padx=10)
reset_button.config(command=click_reset_button)

app.mainloop()
