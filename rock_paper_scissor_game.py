# ROCK-PAPER-SCISSOR  GAME
import random
print("\n๐ฎ๐ฎ๐ฎ๐ฎ๐ฎ๐ฎ๐ฎ๐ฎ Welcome  to ๐๐ด๐ต ROCK ,   ๐๐๐PAPER,   โโโ SCISSOR      Game๐ฎ๐ฎ๐ฎ๐ฎ๐ฎ๐ฎ๐ฎ๐ฎ ")
list1 = ['rock','paper','scissor']
comp_count = 0
user_count = 0 
def player_input():
    global user_count,comp_count
    while (True):                                    # while loop due to particular input by user only, else ask again & again 
        p_choice=str(input("\nEnter your choice:\n for rock:\ttype r\n for paper:\ttype p\n for scissor:   type s\n for exit the game: type 0\n")).lower()
        if (p_choice=='r'):
            p_choice = list1[0]                                       
            return p_choice
        elif (p_choice=='p'):
            p_choice = list1[1]
            return p_choice
        elif (p_choice=='s'):
            p_choice = list1[2]
            return p_choice
        elif (p_choice=='0'):                                        # for exit the game
             print(f'๐๐จ๐ฆ๐ฉ๐ฎ๐ญ๐๐ซ ๐๐จ๐ง : {comp_count}\n๐๐จ๐ฎ ๐๐จ๐ง : {user_count}')
             print('\n๐๐๐๐๐ ไธแผแฉแแแ แดแแ แญแชแฉฦณIแวค ๐๐๐๐๐')
             break
        else:
            print("\nPLEASE enter Correct keyword โโโโโโโโ")
            
def check(p_input,comp_choice):
    global user_count,comp_count                                            # for user_choice = rock, 
    print(f'your choice is {p_input}\ncomputer choice is {comp_choice}')    # there is 3 possibilites with computer choice
    if (p_input==comp_choice):                                               # similary for others
       print('\n**************** โฐโขโโ TIE โโโขโฏ ***************')
    else:
        if (p_input=='rock'):
            if (comp_choice=='paper'):
                print('\n๐๐๐๐๐๐๐๐๐๐ ๐ฒ๐พ๐ผ๐ฟ๐๐๐ด๐ ๐๐พ๐ฝ ๐๐๐๐๐๐๐๐๐๐')
                comp_count +=1
            else:
               print('๐๐๐๐๐๐๐๐๐๐๐๐พ๐ ๐๐พ๐ฝ๐๐๐๐๐๐๐๐๐๐')
               user_count +=1
        if (p_input=='paper'):
            if (comp_choice=='scissor'):
                print('\n๐๐๐๐๐๐๐๐๐๐ ๐ฒ๐พ๐ผ๐ฟ๐๐๐ด๐ ๐๐พ๐ฝ ๐๐๐๐๐๐๐๐๐๐')
                comp_count +=1
            else:
              print('๐๐๐๐๐๐๐๐๐๐๐๐พ๐ ๐๐พ๐ฝ ๐๐๐๐๐๐๐๐๐๐')
              user_count +=1
        if (p_input=='scissor'):
            if (comp_choice=='rock'):
                print('\n๐๐๐๐๐๐๐๐๐๐ ๐ฒ๐พ๐ผ๐ฟ๐๐๐ด๐ ๐๐พ๐ฝ ๐๐๐๐๐๐๐๐๐๐')
                comp_count +=1
            else:
                print('๐๐๐๐๐๐๐๐๐๐๐๐พ๐ ๐๐พ๐ฝ๐๐๐๐๐๐๐๐๐๐')
                user_count +=1

while(True):
    p_input = player_input()                            # calling player input function for user choice      
    comp_choice = random.choice(list1)                  # computer is choosing random values from list1
    if (p_input==None):                                # for Exit purpose
        break
    check(p_input,comp_choice)                        # calling check fun. for user and computer choice
