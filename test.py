import tkinter as tk
import pyautogui
import time

count = 0
run = False


def var_name(mark_local):
    def value():
        if run:
            global count
            show = 'count: {} minutes'.format(count)
            mark_local['text'] = show
            # Increment the count after
            # every 1 second
            mark_local.after(5000, value)
            pyautogui.click(button='right')
            count += 1

    value()


# While Running
def start_timer(mark_local):
    global run
    run = True
    var_name(mark_local)
    start['state'] = 'disabled'
    stop['state'] = 'normal'
    reset['state'] = 'normal'


# While stopped
def stop_timer():
    global run
    start['state'] = 'normal'
    stop['state'] = 'disabled'
    reset['state'] = 'normal'
    run = False


# For Reset
def reset_timer(label):
    global count
    count = -1
    if not run:
        reset['state'] = 'disabled'
        mark['text'] = 'Welcome'
    else:
        mark['text'] = 'Start'


base = tk.Tk()
base.title("Insomnia")
base.minsize(width=300, height=200)

mark = tk.Label(base, text="Welcome", fg="black", font="Times 15 bold", bg="white")
mark.pack()

# label 2
mark_1 = tk.Label(base, text="Start time: ", fg="black", bg="white").pack()

# label 3
mark_2 = tk.Label(base, text="End time:  ", fg="black", bg="white").pack()

start = tk.Button(base, text='Start', width=25, command=lambda: start_timer(mark))
stop = tk.Button(base, text='Stop', width=25, state='disabled', command=stop_timer)
reset = tk.Button(base, text='Quit', width=25, state='disabled', command=lambda: base.destroy())
start.pack()
stop.pack()
reset.pack()

base.mainloop()
