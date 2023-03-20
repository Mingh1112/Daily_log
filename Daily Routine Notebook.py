import datetime
import time
import os 
from time import sleep


def food_log(name):
    with open(f"{name}_food.txt","a+") as file:
        user_diet = input("\n Enter Your Today Diet : ")
        file.write(f" {time.asctime(time.localtime(time.time()))} >> {user_diet.capitalize()} \n")



def excercise_log(name):
    with open(f"{name}_excercise.txt","a+") as file:
        user_exc = input("\n Enter Your Today Excercise : ")
        file.write(f" {time.asctime(time.localtime(time.time()))} >> {user_exc.capitalize()} \n")


def retrive_log(name):
    while True:
        inp = int(input("\n For Cheking User Log :  \n 1. Check Food Log\n 2. Check Excersize Log \n 3. Make Log Again \n 4. Quit\n Enter here : "))
        try:
            if inp ==1 :
                print(f" {name} Log:")
                with open(f"{name}_food.txt") as file:
                    print(file.read())
            elif inp ==2:
                print(f" {name} Log:")
                with open(f"{name}_excercise.txt") as file:
                    print(file.read())
            elif inp ==3:
                break
            elif inp ==4:
                sleep(0.1)
                os.system('cls')
                quit()
            else:
                print("\n Please Enter Valid Input")
        except Exception as e:
             print("\n Please Enter Valid Input",e)


print(""" ______        _ _          ______                   _                _______                  ______              _     
(______)      (_) |        (_____ \              _  (_)              (_______)       _        (____  \            | |    
 _     _ _____ _| |_   _    _____) )___  _   _ _| |_ _ ____  _____    _     _  ___ _| |_ _____ ____)  ) ___   ___ | |  _ 
| |   | (____ | | | | | |  |  __  // _ \| | | (_   _) |  _ \| ___ |  | |   | |/ _ (_   _) ___ |  __  ( / _ \ / _ \| |_/ )
| |__/ // ___ | | | |_| |  | |  \ \ |_| | |_| | | |_| | | | | ____|  | |   | | |_| || |_| ____| |__)  ) |_| | |_| |  _ ( 
|_____/ \_____|_|\_)__  |  |_|   |_\___/|____/   \__)_|_| |_|_____)  |_|   |_|\___/  \__)_____)______/ \___/ \___/|_| \_)
                  (____/                                                                                                 
 ______           _______ _             _     ___   ___   ___   ______                                                   
(____  \         (_______|_)           | |   (___) (___) (___) (_____ \                                                  
 ____)  )_   _    _  _  _ _ ____   ____| |__    _     _     _    ____) )                                                 
|  __  (| | | |  | ||_|| | |  _ \ / _  |  _ \  | |   | |   | |  / ____/                                                  
| |__)  ) |_| |  | |   | | | | | ( (_| | | | |_| |_ _| |_ _| |_| (_____                                                  
|______/ \__  |  |_|   |_|_|_| |_|\___ |_| |_(_____|_____|_____)_______)                                                 
        (____/                   (_____|                                                                                 """)
while True:
    user_input = input("\n Enter client name first to make log and retrive log : ") 
    client_name = user_input.capitalize()   
    try:          
        func = int(input("\n What log do you make :\n 1.Make Food Log\n 2.Make Excercise Log\n 3.Retrive Log\n 4.Quit \n\n Enter Here :  "))
        if func == 1:
            food_log(client_name)
        elif func==2:
            excercise_log(client_name)
        elif func==3:
            retrive_log(client_name)
        elif func ==4:
            print("\n Program Terminated !See you soon")
            sleep(0.1)
            os.system('cls')
            quit()
        else:
            print("\n Please enter valid input.")
    except Exception as e:
         print("\n Please Enter Valid Input",e)

