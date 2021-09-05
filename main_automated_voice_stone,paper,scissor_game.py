import random as random 
import pyttsx3
import speech_recognition as sr

r=sr.Recognizer()



def SpeakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()
    
welcome_text="welcome to Automated Stone paper and scissor game,Designed by Ompodey"

#main game
com_choice=["stone","paper","scissor"]
play_again="yes"
while (play_again=='yes'):
    intro='Welcomr to Stone Paper Scissor'
    intro_detail="A.I POWERED game designed by Om Podey"
    print(intro.center(100,"*"))
    print(intro_detail.center(30))
    SpeakText(welcome_text)
    print('Game start:')
    SpeakText("how many rounds do you want to play?")
    n=int(input('How many rounds do you want to play? Enter the number of rounds'))
    n=str(n)
    SpeakText("ok! you are playing for"+n+"rounds.")
    n=int(n)
    user_won=0
    com_won=0
    for i in range(0,n):
        print("Its your turn, please say your choice [stone ,paper or scissor]")
        SpeakText("Its your turn, please say yor choice ,stone ,paper or scissor")
        deco="-"
        user=''
        comp=''
        try:
            with sr.Microphone() as source2:
                print("Listening ...")
                audio2 = r.listen( source2 ,phrase_time_limit=2.7)
                
                MyText = r.recognize_google( audio2)
                MyText = MyText.lower()
                if "paper" in MyText:
                    print (MyText)
                    user="paper"
                elif "stone"in MyText:
                    print (MyText)
                    user="stone"
                elif "scissor"in MyText:
                    print (MyText)
                    user="scissor"
                else:
                    print("voice identification error!!!")
                    user=input('Enter your choice here:')
        except sr.RequestError as e:
            print("voice identification error!!!")
            user=input('Enter your choice here:')
        except sr.UnknownValueError:
            print("voice identification error!!!")
            user=input('Enter your choice here:')
        print(deco.center(50,"-"))
        comp=random.choice(com_choice)
        print("Your choice:",user)
        print('Computer choice:',comp)
        print(deco.center(50,"-"))
        if (user==comp):
            user_won+=1
            com_won+=1
            print("DRAW (both gets +1 score)")
            SpeakText("Your choice is"+user)
            SpeakText('Computer choice is'+comp)
            SpeakText("Its a tie")
        elif (user=="stone" and comp=="scissor") or (user=="paper" and comp=="stone") or (user=="scissor" and comp=="paper"):
            user_won+=1
            print("You Won!!!")
            SpeakText("Your choice is"+user)
            SpeakText('Computer choice is'+comp)
            SpeakText("Hurrey you won!")
        elif (comp=="stone" and user=="scissor") or (comp=="paper" and user=="stone") or (comp=="scissor" and user=="paper"):
            com_won+=1
            print("Computerr Won!!!")
            SpeakText("Your choice is"+user)
            SpeakText('Computer choice is'+comp)
            SpeakText("Computer won!")
        else:
            print("invalid Entry,(Game exit)/Thank you!")
            
            break
    if user_won==com_won:
        print("Your Score=",user_won)
        print("Computer Score=",com_won)
        user_won=str(user_won)
        com_won=str(com_won)
        SpeakText("Your Score="+user_won)
        SpeakText("Computer Score="+com_won)
        SpeakText("yeah! its a tie")
        print("Its a tie !!!")
    elif user_won>com_won:
        print("Your Score=",user_won)
        print("Computer Score=",com_won)
        user_won=str(user_won)
        com_won=str(com_won)
        SpeakText("Your Score="+user_won)
        SpeakText("Computer Score="+com_won)
        SpeakText("Congradzzz You won!!!")
        print("Congradzzz You won!!!")
    elif user_won<com_won:
        print("Your Score=",user_won)
        print("Computer Score=",com_won)
        user_won=str(user_won)
        com_won=str(com_won)
        SpeakText("Your Score="+user_won)
        SpeakText("Computer Score="+com_won)
        SpeakText("Oh ho you loose , computer WoN!!!")
        print("Oh ho you loose , computer WoN!!!")
    print('Do you want to restart again?\n(yes or no?):')
    SpeakText('Do you want to restart again?(yes or no?)')
    try:
        with sr.Microphone() as source2:
                print("Listening ...")
                audio2 = r.listen( source2 ,phrase_time_limit=3)
                
                MyText = r.recognize_google( audio2)
                MyText = MyText.lower()

                if "yes" in MyText:
                    play_again="yes"
                elif "no" in MyText:
                    play_again="no"
    except:
        print("voice identification error!")
        play_again=input('Do you want to restart again?\n(yes or no?):')
        


        
    
        
                
    
    




        
    
    

            
            
            

    
    
