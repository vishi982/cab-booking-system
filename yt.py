# TAXI APP USING PYTHON 
import random
global_otp = None


def main_display():
    print("Welcome to YOURIDE app")
    print("1: BOOK A RIDE")
    print("2: END A RIDE")
    print("3: CANCEL A RIDE")
    print("4: EXIT")

def main():
    while True:
        main_display()
        choice = input("enter a number between 1-4 to select the option:")

        if choice == "1":
            book_ride()
        elif choice =="2":
            end_ride()
        elif choice =="3":
            cancel_ride()
        elif choice =="4":
            break
        else:
            print("choose correct number")


# 1km = 0.50 dollar
def book_ride():
    global global_otp
    print("1:Car")
    print("2:motor cycle")
    print("3:mini cab")
    print("4: luxury car")
    ride_choice = input("select the number from 1-4 for ride option:")
    if ride_choice == "1":
        print("Simple car selected as youride")
    elif ride_choice =="2":
        print("motorcycle selected as youride")
    elif ride_choice =="3":
        print("mini cab selected as youride")
    elif ride_choice =="4":
        print("luxury car selected as youride")
    else:
        print("choose correct number")
    
    pickup = input("enter your pickup location: ")
    drop_off = input("enter your drop off location: ")
    distance = int(input("enter the approximate distance between these location in kilometer:"))
    print(f"your pickup location is {pickup} and your drop off location is {drop_off}")
    cost = distance * 0.50
    print(f"the total cost for this ride will be ${cost}")
    global_otp = generate_otp()
    print(f"this is your otp which you have to use while cancelling or ending the ride:{global_otp}")
    print("our rider will contact you once he reaches your location")
    print("if the rider doesnot says this otp then dont attend the ride.")
    print("have a safe ride :)")

    
    




def cancel_ride():
    global global_otp
    compare_otp = int(input("enter your otp to end this ride:"))
    if global_otp == compare_otp:
        print("Ride ended successfully!!")
        input("WHY ARE YOU CANCELLING THE RIDE??")
    else:
        print("INVALID OTP ENTERED")
def end_ride():
    global global_otp
    compare_otp = int(input("enter your otp to end this ride:"))
    if global_otp == compare_otp:
        print("Ride ended successfully!!")
        input("rate the ride between 1-5")
    else:
        print("INVALID OTP ENTERED")

def generate_otp():
    otp = random.randint(10000,99999)
    return otp



    


if __name__ == "__main__":
    
    main()
























