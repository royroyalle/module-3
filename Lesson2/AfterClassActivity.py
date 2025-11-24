def shutdown(userinput):
    if userinput == 'Yes' or userinput == 'yes':
        print("Initiating shutdown")
    elif userinput == 'No' or userinput == 'no':
        print("Aborting shutdown")
    else:
        print("Invaild Answer, restart the shutdown")
print("Are you certain that you want to shut down this PC?")
ue = input("Enter Yes or No:")
shutdown(ue)
