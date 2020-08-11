from rivescript import RiveScript
from tkinter import *
chatBot=RiveScript()
chatBot.load_file('response.rive')
chatBot.sort_replies()

win=Tk()
win.title("GO corona")

def send():
    sent="User-->"+message.get()
    chat.insert(END,"\n"+sent)
    reply="Plasma Bot-->"+chatBot.reply("localuser",message.get())
    chat.insert(END,"\n"+reply)
    message.delete(0,END)
chat=Text(win)
chat.grid(row=0,column=0,columnspan=2)
message=Entry(win,width=100)
message.grid(row=1,column=0)
send=Button(win,text="send",command=send).grid(row=1,column=1)
win.mainloop()

