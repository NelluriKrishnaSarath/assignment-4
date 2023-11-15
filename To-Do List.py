from tkinter import *
from tkinter import messagebox

def newTask():
    task = entry.get()
    if task != "":
        lb.insert(END, task)
        entry.delete(0, "end")
    else:
        messagebox.showwarning("warning", "Please add some task.")

def deleteTask():
    lb.delete(ANCHOR)

cs = Tk()
cs.geometry('500x450')
cs.title('To-Do List for Codsoft')
cs.config(bg='grey')
frame = Frame(cs)
frame.pack(pady=10)

lb = Listbox(
    frame,
    width=25,
    height=7,
    font=('Times', 18),
    bd=0,
    fg='grey',
    highlightthickness=0,
    selectbackground='black',
    activestyle="none",

)
lb.pack(side=LEFT, fill=BOTH)

tablelist = [
    'python prommaing',
    'wed development',
    'codsoft',
    
]

for item in tablelist:
    lb.insert(END, item)

sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

entry = Entry(
    cs,
    font=('times', 24)
)

entry.pack(pady=25)

btnframe = Frame(cs)
btnframe.pack(pady=25)

addbt = Button(
    btnframe,
    text='Add Task',
    bg='green',
    padx=25,
    pady=15,
    command=newTask
)
addbt.pack(fill=BOTH, expand=True, side=LEFT)

delbtn = Button(
    btnframe,
    text='Delete Task',
    bg='red',
    padx=25,
    pady=15,
    command=deleteTask
)
delbtn.pack(fill=BOTH, expand=True, side=LEFT)

cs.mainloop()