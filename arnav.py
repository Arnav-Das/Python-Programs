#MADE BY - ARNAV DAS
#Topic - "TRANSPORT"
import os
def no_line(F_NAM):                 # for counting the number of lines in a text file
    file = open(F_NAM,'r')
    count = 0
    for line in file:
        count+=1
    file.close()
    return count
def change_val(F_NAM,LN_NO,NEW):    #for changing the values of a given line of a file
    ofile=open(F_NAM+".txt","r")
    ofile_2=open("temp.txt","w")
    no=0
    for line in ofile:
        no+=1
        if no!=LN_NO:
            ofile_2.write(line)
        else:
            ofile_2.write(NEW)
    ofile.close()
    ofile_2.close()
    os.remove(F_NAM+".txt")
    os.rename("temp.txt",F_NAM+".txt")
def route():                        #for showing the bus route 
    ofile=open("Route.txt","r")
    print ofile.read()
    ofile.close()
def buy():                          #for buying tickets for bus or to buy cabs
    ofile=open("manager.txt","r")
    ofile.readline()
    ofile.readline()
    mony=float(((ofile.readline().rstrip("\n")).split(" : "))[1])#TOTAL MONEY ACCUMULATED
    no=0
    for line in ofile:
        no+=1
        temp=(line.rstrip("\n")).split(" : ")
        if no==1:
            cb_f=temp[1]    #CAB FARE
        elif no==2:
            bsst_f=temp[1]  #BUS SEAT FARE 
        elif no==3:
            absst_f=temp[1] #AC BUS SEAT FARE
        elif no==4:
            cb_t=temp[1]    #TOTAL NUMBER OF CABS
        elif no==6:
            cb_nu=temp[1]   #NUMBER OF CABS NOT IN USE 
        elif no==8:
            bsst_v=temp[1]  #NUMBER OF BUS SEATS VACANT
        elif no==10:
            absst_v=temp[1] #NUMBER OF AC BUS SEATS VACANT
    ofile.close()
    while True:
        choice=raw_input("Enter the type of vehicle you want to buy tickets for(1.CAB , 2.BUS)\n=>")
        if choice.isdigit()and int(choice) in [1,2]:
            if int(choice)==1:
                while True:
                    NO_C=raw_input("Please Enter the number of cabs you need\n=>")
                    if NO_C.isdigit() and int(NO_C) in range(int(cb_nu)+1):
                        Rs=int(cb_f)*int(NO_C)
                        print "The transactions will amount to Rs."+str(Rs)
                        q=raw_input("Do you want to continue(Y/N)\n=>")
                        if q.lower()=="n":
                            continue
                        else:
                            print "You have taken "+NO_C+" cabs on rent for 24 hours."
                            #-------------------------CHANGING VALUES IN DEFAULT FILE----------------------------------
                            change_val("manager",8,"NUMBER OF CABS IN USE : "+str(int(cb_t)-int(cb_nu)+int(NO_C))+"\n")
                            change_val("manager",9,"NUMBER OF CABS NOT IN USE : "+str(int(cb_nu)-int(NO_C))+"\n")
                            change_val("manager",3,"TOTAL MONEY ACCUMULATED : "+str(int(mony)+Rs)+"\n")
                            break
                    elif NO_C.isdigit()!= True:
                        print "Please Enter Numerical Values Only."
                        continue
                    else:
                        print "Sorry, We only have "+cb_nu+"cabs left so Please Enter within this range"
                        continue
                break
            elif int(choice)==2:
                file=open("Route.txt","r")
                file.readline()
                file.readline()
                while True:
                    start=raw_input("Please Enter serial No. for your starting point (or 'route'to see list of bus stops)\n=>")
                    if start.lower()=="route":
                        route()
                        continue
                    stop=raw_input("Please Enter serial No. for your stoppage\n=>")
                    if start.isdigit() and int(start) in range(1,7) and stop.isdigit() and int(stop) in range(1,7):
                        for line in file:
                            temp=line.split("=>")
                            temp_2=(str(temp[1]).rstrip("\n")).split(":     ")
                            if int(temp[0].lstrip(" "))==int(start):
                                strt=str(temp_2[0]).rstrip(" ")
                                srt_tim=str(temp_2[1])
                            if int(temp[0])==int(stop):
                                stp=str(temp_2[0]).rstrip(" ")
                                stp_tim=str(temp_2[1])
                        file.close()
                        dur=abs(int(str(srt_tim.split(":")[0]).lstrip("0")) - int(str(stp_tim.split(":")[0]).lstrip("0")))
                        break
                    else:
                        print"Please enter Numerical value from 1 to 6 only"
                        continue
                while True:
                    bs_typ=raw_input("Enter the type of bus you want to buy tickets for(1.AC BUS , 2.Commercial BUS)\n=>")
                    if bs_typ.isdigit() and int(bs_typ) in [1,2]:
                        if int(bs_typ)==1:
                            while True:
                                NO_st=raw_input("Please enter the No. of seats you want to buy tickets for\n=>")
                                if NO_st.isdigit() and int(NO_st) in range(int(absst_v)+1):
                                    Rs=abs(int(absst_f)*int(NO_st)*dur)
                                    print "The transactions will amount to Rs."+str(Rs)
                                    q=raw_input("Do you want to continue(Y/N)\n=>")
                                    if q.lower()=="n":
                                        continue
                                    else:
                                        print "You have bought "+NO_st+" ac bus tickets from "+strt+" to "+stp
                                        print "boarding time is "+srt_tim+" and arrival time is "+stp_tim
                                        print "The journey will be of "+str(dur)+" hours."
                                        #-----------------------------CHANGING VALUES IN DEFAULT FILE------------------------------------
                                        change_val("manager",3,"TOTAL MONEY ACCUMULATED : "+str(int(mony)+Rs)+"\n")
                                        change_val("manager",12,"NUMBER OF AC BUS SEATS OCCUPIED : "+str(60-int(absst_v)+int(NO_st))+"\n")
                                        change_val("manager",13,"NUMBER OF AC BUS SEATS VACANT : "+str(int(absst_v)-int(NO_st))+"\n")
                                        break
                                elif NO_st.isdigit()!= True:
                                    print "Please Enter Numerical Values Only."
                                    continue
                                else:
                                    print "We only have "+absst_v+"seats left so Please Enter within this range"
                                    continue
                            break
                        elif int(bs_typ)==2:
                            while True:
                                NO_st=raw_input("Please enter the No. of seats you want to buy tickets for\n=>")
                                if NO_st.isdigit() and int(NO_st) in range(int(bsst_v)+1):
                                    Rs=abs(int(bsst_f)*int(NO_st)*dur)
                                    print "The transactions will amount to Rs."+str(Rs)
                                    q=raw_input("Do you want to continue(Y/N)\n=>")
                                    if q.lower()=="n":
                                        continue
                                    else:
                                        print "You have bought "+NO_st+" bus tickets from "+strt.rstrip("\t")+" to "+stp.rstrip("\t")
                                        print "boarding time is "+srt_tim+" and arrival time is "+stp_tim
                                        print "The journey will be of "+str(dur)+" hours."
                                        #--------------------------CHANGING VALUES IN DEFAULT FILE-----------------------------------
                                        change_val("manager",3,"TOTAL MONEY ACCUMULATED : "+str(int(mony)+Rs)+"\n")
                                        change_val("manager",10,"NUMBER OF BUS SEATS OCCUPIED : "+str(60-int(bsst_v)+int(NO_st))+"\n")
                                        change_val("manager",11,"NUMBER OF BUS SEATS VACANT : "+str(int(bsst_v)-int(NO_st))+"\n")
                                        break
                                elif NO_st.isdigit()!= True:
                                    print "Please Enter Numerical Values Only."
                                    continue
                                else:
                                    print "We only have "+bsst_v+"seats left so Please Enter within this range"
                                    continue
                            break
                    elif bs_typ.isdigit()!= True:
                        print "Please Enter Numerical Values Only."
                        continue
                    else:
                        print"Please Enter '1' or '2' only)"
                        continue
                break
        elif choice.isdigit()!= True:
            print "Please Enter Numerical Values Only."
            continue
        else:
            print"Please Enter '1' or '2' only)"
            continue        
    ofile=open("users.txt","a")
    ofile.write(NAM+" : "+str(Rs)+"\n")
    ofile.close()
def rtrn():                 #FOR RETURNING THE TICKETS
    ofile= open("users.txt","r")
    no=0
    cnt=0
    #CHEAKING IF THE USER HAS MADE TRANSACTIONS WITH OUR FIRM IN THE PAST
    for line in ofile:
        no+=1
        temp=(line.rstrip("\n")).split(" : ")
        if NAM==temp[0]:
            Rs=int(temp[1])
            LN_NO=no
        else:
            cnt+=1
    ofile.close()
    if cnt!=no:         #IF THE USER HAS MADE TRANSACTIONS WITH THE FIRM IN THE PAST
        ofile=open("manager.txt","r")
        ofile.readline()
        ofile.readline()
        mony=float(((ofile.readline().rstrip("\n")).split(" : "))[1])
        ofile.close()
        print NAM,",you had made a transaction with us of Rs "+str(Rs)
        print "The refund would be 75% of the total tranaction. ie. Rs"+str(Rs*.75)
        while True:
            q=raw_input("Do you want to continue returning your ticket(Y/N)\n=>")        
            if q.lower()=="y":
                change_val("users",LN_NO,"")
                change_val("manager",3,"TOTAL MONEY ACCUMULATED : "+str(int(mony)-(Rs*.75))+"\n")
                print"your ticket has been refunded"
                break
            elif q.lower()=="n":
                break
            else:
                print"please enter 'y' or 'n' only."
                continue
    else:           #IF THE USER HAS NOT MADE TRANSACTIONS WITH THE FIRM IN THE PAST
        print NAM+",You have never made any transactions with our firm in the past."
def manager():      #for the manager of the firm to make changes to the fares etc.
    ofile=open("manager.txt","r")
    mngrs=(ofile.readline().rstrip("\n")).split(" ")    #NAMES OF THE MANAGERS
    psswrd=ofile.readline().rstrip("\n")                #PASSWORD FOR ENTRY
    mony=float(((ofile.readline().rstrip("\n")).split(" : "))[1])#TOTAL MONEY ACCUMULATED
    cb_f=((ofile.readline().rstrip("\n")).split(" : "))[1]       #CAB FARE
    bsst_f=((ofile.readline().rstrip("\n")).split(" : "))[1]     #CAB FARE
    absst_f=((ofile.readline().rstrip("\n")).split(" : "))[1]    #AC BUS SEAT FARE
    cb_t=((ofile.readline().rstrip("\n")).split(" : "))[1]       #TOTAL NUMBER OF CABS
    ofile.readline()
    cb_nu=((ofile.readline().rstrip("\n")).split(" : "))[1]      #NUMBER OF CABS NOT IN USE
    ofile.close()
    while True:      
        usr_nam=raw_input("Please enter your username\n=>")
        if usr_nam.isalpha():
            if usr_nam.lower() in mngrs:
                print"Username Found"
                break
            else:
                print"Username not found."
                continue
        else:
            print"Please enter alphabetical values only."
            continue
    while True:
        pss=raw_input("Please Enter your password\n=>")
        if pss==psswrd:
            print"Access Granted."
            break
        else:
            print"Password is incorrect."
            continue
    print "Welcome back "+usr_nam+","
    while True:
        print"""What do you want to do;
        1=>Change CAB FARE
        2=>Change BUS FARE
        3=>Change AC BUS FARE
        4=>BUY/SELL CAB
        5=>BACK TO MAIN MENU"""
        choice=raw_input("=>")
        if choice.isdigit() and int(choice) in [1,2,3,4,5]:
            if int(choice)==1:
                print"The previous CAB FARE was "+cb_f+"Rs."
                NEW=raw_input("Please Enter new CAB FARE\n=>")
                if NEW.isdigit():
                    #------CHANGING VALUES IN DEFAULT FILE-------
                    change_val("manager",4,"CAB FARE : "+NEW+"\n")
                    print "CAB FARE has been changed"
                    continue
                else:
                    print"Please enter Numerical Value for the CAB FARE"
                    continue
            elif int(choice)==2:
                print"The previous BUS FARE was "+bsst_f+"Rs."
                NEW=raw_input("Please Enter new BUS FARE\n=>")
                if NEW.isdigit():
                    #------CHANGING VALUES IN DEFAULT FILE-------
                    change_val("manager",5,"BUS FARE : "+NEW+"\n")
                    print "BUS FARE has been changed"
                    continue
                else:
                    print"Please enter Numerical Value for the BUS FARE"
                    continue
            elif int(choice)==3:
                print"The previous AC BUS FARE was "+absst_f+"Rs."
                NEW=raw_input("Please Enter new BUS FARE\n=>")
                if NEW.isdigit():
                    #------CHANGING VALUES IN DEFAULT FILE-------
                    change_val("manager",6,"AC BUS FARE : "+NEW+"\n")
                    print "AC BUS FARE has been changed"
                    continue
                else:
                    print"Please enter Numerical Value for the BUS FARE"
                    continue
            elif int(choice)==4:
                by_sl=raw_input("Enter (1.BUY , 2.SELL)\n=>")
                if by_sl.isdigit() and int(by_sl)==1:
                    print usr_nam+"You have "+str(mony)+"Rs. left."
                    print"""One cab is worth Rs.50000
                    so you can buy """+str(int(mony)//50000)+"cabs."
                    NEW=raw_input("Please Enter the number of cabs you want to buy\n=>")
                    if NEW.isdigit() and int(NEW) in range((int(mony)//50000)+1):
                        #-------------------------CHANGING VALUES IN DEFAULT FILE-------------------------------
                        change_val("manager",3,"TOTAL MONEY ACCUMULATED : "+str(int(mony)-(int(NEW)*50000))+"\n")
                        change_val("manager",7,"NUMBER OF CABS : "+str(int(cb_t)+int(NEW))+"\n")
                        change_val("manager",9,"NUMBER OF CABS NOT IN USE : "+str(int(cb_nu)+int(NEW))+"\n")
                        print NEW+" Cabs has been bought."
                        continue
                    else:
                        print "Please Enter Numerical values between 0 to "+str(int(mony)//50000)+" only"
                        continue
                elif by_sl.isdigit() and int(by_sl)==2:
                    print usr_nam+"You have "+cb_t+" cabs left."
                    print"One cab is sold at 75% of the toal MRP, ie. Rs.50000"
                    NEW=raw_input("Please Enter the number of cabs you want to sell\n=>")
                    if NEW.isdigit() and int(NEW) in range(int(cb_t)+1):
                        #---------------------------CHANGING VALUES IN DEFAULT FILE---------------------------------
                        change_val("manager",3,"TOTAL MONEY ACCUMULATED : "+str(int(mony)+(int(NEW)*.75*50000))+"\n")
                        change_val("manager",7,"NUMBER OF CABS : "+str(int(cb_t)-int(NEW))+"\n")
                        change_val("manager",9,"NUMBER OF CABS NOT IN USE : "+str(int(cb_nu)-int(NEW))+"\n")
                        print NEW+" Cabs has been sold."
                        continue
                    else:
                        print "Please Enter Numerical values between 0 to "+cb_t+" only"
                        continue
            elif int(choice)==5:
                break
        else:
            print"Please enter numerical values between 1 to 5."
            continue
#---------------------------------MAIN PROGRAM-------------------------------------------
print "\t\t\tWELCOME TO ARNAV TRANSPORTS"
NAM=raw_input("Please Enter Your Name\n=>")
def main():
    try:
        while True:
            print"""What do you want to do;
            1=>BUY TICKETS
            2=>RETURN TICKETS
            3=>ROUTE
            4=>OTHER
            5=>QUIT"""
            choice=raw_input("=>")
            if choice.isdigit() and int(choice) in range(1,6):
                if int(choice)==1:
                    buy()
                    continue
                elif int(choice)==2:
                    rtrn()
                    continue
                elif int(choice)==3:
                    route()
                    continue
                elif int(choice)==4:
                    print"This setction is for managers only."
                    q=raw_input("Enter 'ok' to go ahead ( or enter any key to go back )\n=>")
                    if q.lower()=="ok":
                        manager()
                        continue
                    else:
                        continue
                elif  int(choice)==5:
                    ofile=open("manager.txt","r")
                    ofile.readline()
                    ofile.readline()
                    ofile.readline()
                    ofile.readline()
                    ofile.readline()
                    ofile.readline()
                    cb_t=((ofile.readline().rstrip("\n")).split(" : "))[1]
                    ofile.close()
                    #-----------------CHANGING VALUES IN DEFAULT FILE------------------------
                    change_val("manager",8,"NUMBER OF CABS IN USE : "+str(0)+"\n")
                    change_val("manager",9,"NUMBER OF CABS NOT IN USE : "+str(cb_t)+"\n")
                    change_val("manager",10,"NUMBER OF BUS SEATS OCCUPIED : "+str(0)+"\n")
                    change_val("manager",11,"NUMBER OF BUS SEATS VACANT : "+str(60)+"\n")
                    change_val("manager",12,"NUMBER OF AC BUS SEATS OCCUPIED : "+str(0)+"\n")
                    change_val("manager",13,"NUMBER OF AC BUS SEATS VACANT : "+str(60)+"\n")
                    print"BYE. VISIT AGAIN."
                    break
            else:
                print"Enter Numerical values between '1' to '5' only."
                continue
    except:         #for unexpected errors
        print"There was an unexpected error\nThe system has rebooted."
        print "-"*100
        print "\t\t\tWELCOME TO ARNAV TRANSPORTS"
        NAM=raw_input("Please Enter Your Name\n=>")
        main()
main()