import time
from pydictionary import Dictionary
from win10toast_click import ToastNotifier
from random_word import RandomWords
import webbrowser
if __name__ == "__main__":
    Noti=ToastNotifier()
    while True:
        a=RandomWords().get_random_word()
        Z=Dictionary(a)
        Y=Z.meanings()
        if len(Y)>0:
            # def calc():                   #function to print meanings,antonyms and synonyms when user clicks on the notification
            #     X=Dictionary(a)
            #     X.print_meanings()
            #     X.print_antonyms()
            #     X.print_synonyms()

            def translate():
                try:
                    webbrowser.open('https://www.google.com')
                except:
                    print('Error')


            Noti.show_toast('New word!: '+a,'Meaning:'+Y[0],duration=10,callback_on_click=translate)
            #using win10toast_click module to display notification instead of plyer module
            #callback_on_click is the argument used to make the notification interactive when we click
            #here we called a function to open google.com;we can some other method to display the meanings,synonyms and 
            #antonyms
