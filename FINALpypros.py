import time
from threading import Thread
from tkinter import *
from pydictionary import Dictionary
from PIL import ImageTk,Image
from random_word import RandomWords
from win10toast_click import ToastNotifier


#creating instance
root=Tk()
root.title('VOCAB A-Z')
root.geometry('600x750')
root.resizable('False','False')

#adding a frame(home screen) and bg img
Home_win=Frame(root,width=600,height=750)
Home_win.pack()
img =Image.open("C:\Endterm Project/vocabA-z.png")
img=img.resize((600,750),Image.ANTIALIAS)
img_pic=ImageTk.PhotoImage(img)
backg=Label(Home_win, image = img_pic)
backg.pack()

#func to access dictionary window
def New_win1():
    Home_win.pack_forget()
    next_win.pack()

#func to access reminder window
def New_win2():
    Home_win.pack_forget()
    next_win1.pack()

#button for dict
Home_Button1=Button(Home_win,text='GO to dictionary',bg='yellow1',borderwidth=6,relief=RAISED,padx=7,pady=4,command=New_win1,font=("Cooper,bold"))
Home_Button1.place(relx=0.35,rely=0.75)

#button for reminder
Home_Button2=Button(Home_win,text='Word Reminder',bg='yellow1',borderwidth=6,relief=RAISED,padx=9,pady=4,command=New_win2,font=("Cooper,bold"))
Home_Button2.place(relx=0.35,rely=0.835)

#func to search and display a ,s and m
def lookup():
    my_text.delete(1.0,END)
    dict=Dictionary(en_try.get())
    X=dict.meanings()
    X1=dict.antonyms()
    X2=dict.synonyms()
    j=1
    if len(X)==0:
        my_text.insert(END,'\nGiven word does not exist!Please, check the spelling of the word or Enter a new word.')
    else:
        my_text.insert(END,'Meanings :\n\n')
        for i in X:
            my_text.insert(END,f'{j}) {i}\n\n')
            j+=1
        my_text.insert(END,"    ______________________________________________________________")
        my_text.insert(END,'\n\n\nAntonyms :\n\n')
        j=1
        if len(X1)==0:
            my_text.insert(END,'Given word has no antonym.\n\n')
        else:
            for i in X1:
                my_text.insert(END,f'{j}) {i}\n\n')
                j+=1
        my_text.insert(END,"    ______________________________________________________________")
        my_text.insert(END,'\n\n\nSynonyms :\n\n')
        j=1
        if len(X2)==0:
            my_text.insert(END,'Given word has no synonyms.\n\n')
        else:
            for i in X2:
                my_text.insert(END,f'{j}) {i}\n\n')
                j+=1

#frame for dict window
next_win=Frame(root,width=600,height=750)
my_label=LabelFrame(next_win,text='Enter your word:',font="Courier,bold",borderwidth=2,relief=GROOVE)
my_label.pack(pady=22,fill=Y)
en_try=Entry(my_label,font=('Tekton Pro Cond',16),borderwidth=5)
en_try.grid(row=0,column=0,padx=10,pady=10)

button1=Button(my_label,text="Search",background='grey',command=lookup,borderwidth=6)
button1.grid(row=0,column=1,padx=10)

#func to return from dic to home
def back_toHome1():
    next_win1.pack_forget()
    Home_win.pack()

#func to return from reminder to home
def back_toHome():
    next_win.pack_forget()
    Home_win.pack()

#button for dict to home
button2=Button(next_win,text='Back',bg='grey',borderwidth=6,relief=RAISED,command=back_toHome)
button2.place(relx=0.03,rely=0.1,relwidth=0.1)

#output screen for dictionaryyy!
my_text=Text(next_win,height=70,width=65,wrap=WORD,font=('comicsansms',11))
my_text.pack()

#frame for reminder
next_win1=Frame(root,width=600,height=750)
img_2 =Image.open("C:/Endterm Project/rem2.jpg")                           #changes
img_2=img_2.resize((600,750),Image.ANTIALIAS)
img_pic2=ImageTk.PhotoImage(img_2)
backg=Label(next_win1, image = img_pic2)
backg.pack()

#MESSAGE TO USER
mssg_to_user=Label(next_win1,text='ENTER THE TIME AFTER WHICH YOU WANT\nTO GET NOTIFIED FOR A NEW ENGLISH WORD\n',background='grey',borderwidth='5',relief=RAISED,padx=5,pady=3,font=('ariel',11))
mssg_to_user.place(relx=0.25,rely=0.05)

#ENTRY BOX
hr2user=Label(next_win1,text='No. of Hour(s): ',font=('ariel',9,'bold'),width=13)
hr2user.place(relx=0.29,rely=0.18)
min2user=Label(next_win1,text='No. of Minute(s): ',font=('ariel',9,'bold'))
min2user.place(relx=0.29,rely=0.23)
Entry_min=Entry(next_win1)
Entry_min.place(relx=0.47,rely=0.23,relwidth=0.1)
Entry_hour=Entry(next_win1)
Entry_hour.place(relx=0.46,rely=0.18,relwidth=0.1)
#notify buttton along with it function

totaltime=0
#toaltime=(hh*60*60)+(mm*60)-10
def notifyme():
    totaltime=int(Entry_hour.get())*60*60+int(Entry_min.get())*60#calculating time delay to notify the user
    global i
    i=False
    while not(i):
            noti=ToastNotifier()
            global Random_wordz
            Random_wordz=RandomWords().get_random_word()
            # Random_wordz='Cat'
            Z=Dictionary(Random_wordz)
            Ynoti=Z.meanings()
            def dispdata():
                my_text.delete('1.0','end')
                dict2=Dictionary(Random_wordz)
                Y=dict2.meanings()
                Y1=dict2.antonyms()
                Y2=dict2.synonyms()
                next_win1.pack_forget()
                next_win.pack()
                k=1
                my_text.insert(END,'WORD : '+Random_wordz.capitalize()+'\n\n')
                if len(Y)==0:
                    my_text.insert(END,'\nGiven word does not exist!Please, check the spelling of the word or Enter a new word.')
                else:
                    my_text.insert(END,'Meanings :\n\n')
                for i in Y:
                    my_text.insert(END,f'{k}) {i}\n\n')
                    k+=1
                my_text.insert(END,"    ______________________________________________________________")
                my_text.insert(END,'\n\n\nAntonyms :\n\n')
                k=1
                if len(Y1)==0:
                    my_text.insert(END,'Given word has no antonym.\n\n')
                else:
                    for i in Y1:
                        my_text.insert(END,f'{k}) {i}\n\n')
                        k+=1
                my_text.insert(END,"    ______________________________________________________________")
                my_text.insert(END,'\n\n\nSynonyms :\n\n')
                k=1
                if len(Y2)==0:
                    my_text.insert(END,'Given word has no synonyms.\n\n')
                else:
                    for i in Y2:
                        my_text.insert(END,f'{k}) {i}\n\n')
                        k+=1
    
            if len(Ynoti)>0:
                # noti.show_toast('NEW WORD!: '+Random_wordz,'MEANING: /n'+''+ Y[0], duration=0)
                noti.show_toast('Click anywhere to know more!'+'\n'+f'New Word: {Random_wordz.capitalize()}',f'Meaning:{Ynoti[0]}',    
                duration=5,callback_on_click=dispdata)
                if totaltime==0:
                    time.sleep(totaltime)
                else:
                    time.sleep(totaltime-10)
noti1=ToastNotifier()             
def stop_notifyme():#func to stop notifying
    global i
    i=True
    root.destroy()
t1=Thread(target=notifyme,daemon=True)
def notithread():
    if Entry_min.get().isdigit() and Entry_hour.get().isdigit(): #it will only start the thread when both the inputs are integer type  
        t1.start()
    else:
        noti1.show_toast('IMPORTANT ALERT!','PLEASE ENTER NUMBERS AS INPUT. ALSO CHECK THAT THEY ARE NON-DECIMAL',duration=1)  
                   
notify_button=Button(next_win1,text='NOTIFY ME!',borderwidth=8,relief=RAISED,command=notithread,font=('ariel',12,'bold'),height=3,width=10,bg='grey')
notify_button.place(relx=0.45,rely=0.32)

stopnotify_button=Button(next_win1,text='STOP NOTIFYING!',borderwidth=8,relief=RAISED,command=stop_notifyme,font=('ariel',12,'bold'),height=3,width=15,bg='grey')
stopnotify_button.place(relx=0.43,rely=0.46)

#button for reminder to home
button3=Button(next_win1,text='Back',bg='grey',borderwidth=6,relief=RAISED,command=back_toHome1)
button3.place(relx=0.045,rely=0.05,relwidth=0.1)
root.mainloop()
