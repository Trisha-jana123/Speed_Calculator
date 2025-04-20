from time import *
import random as r

def mistake(paratest,usertest):
    error = 0
    for i in range(len(paratest)):
        try:
            if paratest[i] != usertest[i]:
                error = error + 1
        except:
            error = error + 1   
    return error     

def speed_time(time_s,time_e,userinput):
    time_delay = time_e - time_s
    time_R = round(time_delay,2)
    speed = len(userinput)/time_R
    return round(speed)
if __name__ == '__main__':
    
    while True:
        check = input(" ready to test : yes / no: ")
        if check == "yes":
            test = ["Python is an amazing language to code where we learn many different functions to learn and make projects.",
            "my name is Trisha Jana","welcome to the world of python"]
            test1 = r.choice(test )
            print("     ***** typing speed *****     ")
            print(test1)
            print()
            print()
            time_1 = time()
            testinput = input(" Enter : ")
            time_2 = time()
        
            print("Speed : ",speed_time(time_1,time_2,testinput)," w/sec")
            print("Error : ",mistake(test1,testinput))

        elif check == "no":
            print(" thank you ")
            break

        else:
            print(" wrong input ")
