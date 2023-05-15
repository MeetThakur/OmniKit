import customtkinter
import tkinter
from bs4 import BeautifulSoup as b
import requests
from tkinter import filedialog as fd
from tkinter import messagebox
import math


meaning = "Search something"


def findmeaning(text):
    try:
        req1 = requests.get("https://www.google.com/search?q=define+"+text)
        soup1 = b(req1.text,"html.parser")
        s = soup1.find("div",class_="Gx5Zad xpd EtOod pkphOe")
        result = s.text
        if result.startswith("Name"):
            temp = result.split(":")
            temp2 = temp[2].split(".")
            return temp2[0]
        elif result.startswith("Did you mean"):
            temp = result.split(":")
            t = temp[1]
            result = findmeaning(t[8:])
            return result
        elif result.startswith("Showing results for") or result.startswith("People also ask") or "askWhat" in result:
            return "Sorry, Meaning Not Found"
        else:
            rl = result.split(".")
            result = rl[0]
            return result

    except requests.exceptions.ConnectionError:
        return 'Error make sure to have a internet Connection'





customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")








Font = ("Comic Sans MS", 16)
f = ("Comic Sans MS",19,"bold")
def mean():
    global meaning
    word = inputWord.get()
    meaningLabel.configure(text=findmeaning(word),wraplength=300,font=Font)





app = customtkinter.CTk()
app.geometry("350x500")
app.grid_rowconfigure(0, weight=1)  # configure grid system
app.grid_columnconfigure(0, weight=1)




tabview = customtkinter.CTkTabview(master=app)
tabview.grid(sticky="nsew",padx=10,pady=10)
t1 = tabview.add("Dictionary") 
t2 = tabview.add("Canvas")
t3 = tabview.add("NotePad")
t4 = tabview.add("Calculator")
tabview.set("Dictionary")



inputWord = customtkinter.CTkEntry(t1,placeholder_text="Enter a word",width=200,height=30,border_width=3,corner_radius=15)
inputWord.place(relx=0.5,rely=0.15,anchor="n")

SearchBtn = customtkinter.CTkButton(t1,text="search",width=120,height=40,command=mean,corner_radius=25,border_width=1)
SearchBtn.place(relx=0.5,rely=0.3,anchor="n")

meaningLabel = customtkinter.CTkLabel(t1,text=meaning)
meaningLabel.place(relx=0.5,rely=0.5,anchor="n")

meaningText = customtkinter.CTkLabel(t1,text="Dictionary")
meaningText.place(relx=0.5,rely=0.01,anchor="n")
meaningText.configure(font=f)













fnt = ("comic sans",10,"bold")
canvas = tkinter.Canvas(t2, width=500, height=500, bg="#2b2b2b")
stroke = 2
def red():
    global color,strokeWid
    strokeWid = 5
    color = "red"
def blue():
    global color,strokeWid
    strokeWid = 5
    color = "blue"
def yello():
    global color,strokeWid
    strokeWid = 5
    color = "yellow"
def green():
    global color,strokeWid
    strokeWid = 5
    color = "lime"
def white():
    global color,strokeWid
    strokeWid = 5
    color = "white"
def redl():
    global color,strokeWid
    strokeWid = 5
    color = "#FD3A4A"

def eraser():
    global color,strokeWid
    color = "#2b2b2b"
    strokeWid = 50


color = "white"

button1 = tkinter.Button(t2,height=2,width=5,bg="white",command=white)
button2 = tkinter.Button(t2,height=2,width=5,bg="blue",command=blue)
button3 = tkinter.Button(t2,height=2,width=5,bg="yellow",command=yello)
button4 = tkinter.Button(t2,height=2,width=5,bg="lime",command=green)
button5 = tkinter.Button(t2,height=2,width=5,bg="red",command=red)
button6 = tkinter.Button(t2,height=2,width=5,bg="white",text="Erase",command=eraser)



canvas.create_window(25,30, window=button1)
canvas.create_window(175,30, window=button2)
canvas.create_window(125,30, window=button3)
canvas.create_window(225,30, window=button4)
canvas.create_window(75,30, window=button5)
canvas.create_window(275,30,window=button6)

strokeWid = 5
def start_draw(event):
    canvas.lastx, canvas.lasty = event.x, event.y

def draw(event):
    canvas.create_line(canvas.lastx, canvas.lasty, event.x, event.y, fill=color, width=strokeWid)
    canvas.lastx, canvas.lasty = event.x, event.y



canvas.bind("<Button-1>", start_draw)
canvas.bind("<B1-Motion>", draw)
canvas.pack(fill="both", expand="YES")












opfile = None
def openfile():
    global filename,opfile
    try:
        filetypes = (('text files', '*.txt'),('All files', '*.*'))
        filename = fd.askopenfilename(filetypes=filetypes)
        if filename.endswith(".txt"):
            opfile = filename
        NotepadEntry.delete("0.0","end")
        with open(filename,"r") as file:
            data = file.read()
        NotepadEntry.insert("1.0",data)
    except:
        filename = opfile
        pass


def savefile():
    global filename,opfile
    try:
        filetypes = (('text files', '*.txt'),('All files', '*.*'))
        filename = fd.asksaveasfilename(filetypes=filetypes)
        if filename.endswith(".txt"):
            opfile = filename
        with open(filename,"w") as file:
            data = NotepadEntry.get("0.0","end")
            file.write(data)
    except:
        filename = opfile
        pass


def save():
    try:
        with open(filename,"w") as file:
            file.write(NotepadEntry.get("0.0","end"))
    except:
        messagebox.showerror("error", "Open a File first")
    


NotepadEntry = customtkinter.CTkTextbox(t3,font=Font)
NotepadEntry.place(x=0,y=50,relheight=1,relwidth=1)
openButton = customtkinter.CTkButton(t3,height=30,width=30,text="Open",command=openfile)
openButton.place(x=0,y=0)
savebutton = customtkinter.CTkButton(t3,height=30,width=30,text="Save",command=save)
savebutton.place(x=50,y=0)
saveasbutton = customtkinter.CTkButton(t3,height=30,width=30,text="Save as",command=savefile)
saveasbutton.place(x=100,y=0)










eq = ' '
brack = 0
def btnClick(btn):
    global eq,brack

    calinput.insert("end",btn._text)
    while brack>0 and btn._text.isdigit()==False:
        eq += ")"
        brack-=1
    eq += btn._text


buttonFrame = customtkinter.CTkFrame(t4,height=450,width=330)
buttonFrame.pack()

calinput = customtkinter.CTkEntry(buttonFrame,height=30,width=300,justify='right',font=f)
calinput.grid(row=1,columnspan=6,padx=10,pady=10)


def equal():
    global eq,brack
    while brack>0:
        eq += ")"
        brack-=1
    calinput.delete('0','end')
    try:
        calinput.insert('end',str(eval(eq))[0:50])
    except:
        calinput.insert('end','error')
    eq = str(eval(eq))[0:50]

def clear():
    global eq
    calinput.delete('0','end')
    eq = ''

def sqroot():
    global brack,eq
    calinput.insert("end",root._text)
    eq += "math.sqrt("
    brack += 1

def square():
    global eq
    calinput.insert('end','^')
    eq += '**'

def trg(btn):
    global eq,brack
    calinput.insert("end",btn._text)
    if btn._text == 'sin':        
        eq += "math.sin(math.radians("
        brack+=2

    elif btn._text == 'cos':
        eq +='math.cos(math.radians('
        brack+=2

    elif btn._text == 'tan':
        eq +='math.tan(math.radians('
        brack+=2


def log(btn):
    global eq,brack
    calinput.insert("end",btn._text)
    if btn._text == 'ln':        
        eq += "math.log("
        brack+=1
    elif btn._text == 'log':
        eq +='math.log10('
        brack+=1





cbutton = customtkinter.CTkButton(buttonFrame,corner_radius=0,height=55,width=55,text='C',font=f,command=clear)
cbutton.grid(row=2,column=4,padx=5,pady=3)

one = customtkinter.CTkButton(buttonFrame,corner_radius=0,height=55,width=55,text='1',font=f,command = lambda: btnClick(one))
one.grid(row=2,column=1,padx=3,pady=3)

two = customtkinter.CTkButton(buttonFrame,corner_radius=0,height=55,width=55,text='2',font=f,command = lambda: btnClick(two))
two.grid(row=2,column=2,padx=3,pady=3)

three = customtkinter.CTkButton(buttonFrame,corner_radius=0,height=55,width=55,text='3',font=f,command = lambda: btnClick(three))
three.grid(row=2,column=3,padx=3,pady=3)




four = customtkinter.CTkButton(buttonFrame,corner_radius=0,height=55,width=55,text='4',font=f,command = lambda: btnClick(four))
four.grid(row=3,column=1,padx=3,pady=3)

five = customtkinter.CTkButton(buttonFrame,corner_radius=0,height=55,width=55,text='5',font=f,command = lambda: btnClick(five))
five.grid(row=3,column=2,padx=3,pady=3)

six = customtkinter.CTkButton(buttonFrame,corner_radius=0,height=55,width=55,text='6',font=f,command = lambda: btnClick(six))
six.grid(row=3,column=3,padx=3,pady=3)

equal = customtkinter.CTkButton(buttonFrame,corner_radius=0,height=55,width=55,text='=',font=f,command = equal)
equal.grid(row=3,column=4,padx=3,pady=3)




seven = customtkinter.CTkButton(buttonFrame,corner_radius=0,height=55,width=55,text='7',font=f,command = lambda: btnClick(seven))
seven.grid(row=4,column=1,padx=3,pady=3)

eight = customtkinter.CTkButton(buttonFrame,corner_radius=0,height=55,width=55,text='8',font=f,command = lambda: btnClick(eight))
eight.grid(row=4,column=2,padx=3,pady=3)

nine = customtkinter.CTkButton(buttonFrame,corner_radius=0,height=55,width=55,text='9',font=f,command = lambda: btnClick(nine))
nine.grid(row=4,column=3,padx=3,pady=3)

plus = customtkinter.CTkButton(buttonFrame,corner_radius=0,height=55,width=55,text='+',font=f,command = lambda: btnClick(plus))
plus.grid(row=4,column=4,padx=3,pady=3)




zero = customtkinter.CTkButton(buttonFrame,corner_radius=0,height=55,width=55,font=f,text='0',command = lambda: btnClick(zero))
zero.grid(row=5,column=1,padx=3,pady=3)

dzero = customtkinter.CTkButton(buttonFrame,corner_radius=0,height=55,width=55,font=f,text='00',command = lambda: btnClick(dzero))
dzero.grid(row=5,column=2,padx=3,pady=3)

deci = customtkinter.CTkButton(buttonFrame,corner_radius=0,height=55,width=55,font=f,text='.',command = lambda: btnClick(deci))
deci.grid(row=5,column=3,padx=3,pady=3)

minus = customtkinter.CTkButton(buttonFrame,corner_radius=0,height=55,width=55,font=f,text='-',command = lambda: btnClick(minus))
minus.grid(row=5,column=4,padx=3,pady=3)





root = customtkinter.CTkButton(buttonFrame,corner_radius=0,height=55,width=55,font=f,text='√',command= sqroot)
root.grid(row=6,column=1,padx=3,pady=3)

square = customtkinter.CTkButton(buttonFrame,corner_radius=0,height=55,width=55,font=f,text='^',command=square)
square.grid(row=6,column=2,padx=3,pady=3)

div = customtkinter.CTkButton(buttonFrame,corner_radius=0,height=55,width=55,font=f,text='/',command = lambda: btnClick(div))
div.grid(row=6,column=3,padx=3,pady=3)

mult = customtkinter.CTkButton(buttonFrame,corner_radius=0,height=55,width=55,font=f,text='*',command = lambda: btnClick(mult))
mult.grid(row=6,column=4,padx=3,pady=3)




logb = customtkinter.CTkButton(buttonFrame,corner_radius=0,height=55,width=55,font=f,text='log',command= lambda: log(logb))
logb.grid(row=7,column=1,padx=3,pady=3)

tan = customtkinter.CTkButton(buttonFrame,corner_radius=0,height=55,width=55,font=f,text='tan',command= lambda: trg(tan))
tan.grid(row=7,column=2,padx=3,pady=3)

sin = customtkinter.CTkButton(buttonFrame,corner_radius=0,height=55,width=55,font=f,text='sin',command = lambda: trg(sin))
sin.grid(row=7,column=3,padx=3,pady=3)

cos = customtkinter.CTkButton(buttonFrame,corner_radius=0,height=55,width=55,font=f,text='cos',command = lambda: trg(cos))
cos.grid(row=7,column=4,padx=3,pady=3)



app.attributes('-topmost',True)
app.mainloop()
