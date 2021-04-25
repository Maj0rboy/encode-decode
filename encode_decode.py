from tkinter import *
import base64
root = Tk()
root.title("Message Encode Decode")
root.geometry("400x400")
# root.config(bg="green")
# header label
mylabel1 = Label(root,text="ENCODE DECODE",font="bold")
mylabel1.place(x=120,y=0)

mylabel2 = Label(root,text="MESSAGE")
mylabel2.place(x=50,y=50)

mylabel3 = Label(root,text="KEY")
mylabel3.place(x=50,y=80)

mylabel4 = Label(root,text="MODE(e-encode,d-decode")
mylabel4.place(x=50,y=120)

# message entry
text = StringVar()
mylabel5 = Entry(root,textvariable=text,width=20)
mylabel5.place(x=220,y=50)

private_key = StringVar()
mylabel6 = Entry(root,textvariable=private_key,width=20)
mylabel6.place(x=220,y=80)

mode = StringVar()
mylabel7 = Entry(root,textvariable=mode,width=20)
mylabel7.place(x=220,y=120)

result = StringVar()
mylabel8 = Entry(root,textvariable=result,width=20)
mylabel8.place(x=220,y=150)


# functions
# encode function
def ENCODE(key,message):
    enc=[]
    for i in range(len(message)):
        key_c = key[i % len(key)]
        enc.append(chr(ord(message[i]) + ord(key_c) % 256))
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

# decode function 
def DECODE(key,message):
    dec = []
    message = base64.urlsafe_b64decode(message).decode()
    for i in range(len(message)):
        key_c = key[i % len(key)]
        dec.append(chr(256 + ord(message[i]) - ord(key_c) % 256))
    return "".join(dec)

# mode function
def Mode():
    if (mode.get() == 'e'):
        result.set(ENCODE(private_key.get(), text.get()))
    elif (mode.get() == 'd'):
        result.set(DECODE(private_key.get(), text.get()))
    else:
        result.set("invalid mode")
# reset function
def reset():
    text.set("")
    private_key.set("")
    mode.set("")
    result.set("")
    
# exit function
def exit():
    root.destroy()

btn_result = Button(root,text="RESULT",relief="solid",width=5,command=Mode)
btn_result.place(x=50,y=150)

btn_reset = Button(root,text="RESET",relief="solid",bg="green",width=5,command=reset)
btn_reset.place(x=120,y=200)

btn_exit = Button(root,text="EXIT",relief="solid",bg="orange",width=5,command=exit)
btn_exit.place(x=200,y=200)

root.mainloop()