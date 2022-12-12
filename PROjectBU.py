import time
from plyer import notification
from random_word import RandomWords
from pydictionary import Dictionary
if __name__ == "__main__":
    i=0
    
    #a='slyly'
    
    # Y1=X.antonyms()
    # Y2=X.synonyms()
    while i<3:
        #a=RandomWords().get_random_word()
        a='Express'
        X=Dictionary(a)
        Y=X.meanings()
        # if len(y)<
        notification.notify(title='New Word!\n'+a,message=f'Meaning:{Y[0]}',
        timeout=2)
        time.sleep(5)
        i+=1


