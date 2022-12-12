import time
from plyer import notification
from random_word import RandomWords
from pydictionary import Dictionary
if __name__ == "__main__":
    i=0
    while i<3:
        a=RandomWords().get_random_word()
        # a='Egfhtftggggfress'
        X=Dictionary(a)
        Y=X.meanings()
        # X.print_meanings()
        # Y1=X.antonyms()
        # Y2=X.synonyms()
        # print(Y)
        count=0
        for k in Y:
            for j in k:
                count+=1
        # print(count)
        if len(Y)>0:
        #     if (count+len(Y)+1)<=256:
        #         notification.notify(title='New Word!\n'+a,message=f'Meaning:{Y}',
        #         timeout=5)
        #         time.sleep(10)
        #         i+=1
        #     else:
                    # if len(Y1)!=0 and len(Y[0])+len(Y1[0])<256:
                    # if len(Y[0])<256:
                    # notification.notify(title='New Word!\n'+a,message=f'Meaning:{Y[0]}\n Antonym: {Y1[0]}',
                    # timeout=5)
                    for n in range(len(Y)):
                        if len(Y[n])<=256:
                            notification.notify(title='New Word!\n'+a,message=f'Meaning:{Y[n]}',
                            timeout=5)
                            # t1 =eval(input("Enter the time by which you want next word (in Hrs)"))
                            # time.sleep(t1*60*60)
                            time.sleep(10)
                            i+=1
                        break
        else:
            pass