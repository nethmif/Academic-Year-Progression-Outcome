Progress=0  # displays the number of students (progress count) in the histogram
Trailer=0   # displays the number of students (trailer count) in the histogram
Retriever=0 # displays the number of students (retriever count) in the histogram
Exclude=0   # displays the number of students (exclude count) in the histogram
Progress_List=[] #stores the progress outcome values entered by the user
Trailer_List=[] #stores the trailer outcome values entered by the user
Retriever_List=[]  #stores the retriever outcome values entered by the user
Exclude_List=[] #stores the exclude outcome values entered by the user
StdID={}
while True:
    Pass=[120,100,100,80,80,80,60,60,60,60,40,40,40,40,40,20,20,20,20,20,20,0,0,0,0,0,0,0]  #list of possible Pass values 
    Defer=[0,20,0,40,20,0,60,40,20,0,80,60,40,20,0,100,80,60,40,20,0,120,100,80,60,40,20,0] #list of possible Defer values     
    Fail=[0,0,20,0,20,40,0,20,40,60,0,20,40,60,80,0,20,40,60,80,100,0,20,40,60,80,100,120]  #list of possible Fail values
    Outcome=["Progress","Progress (module trailer)","Progress (module trailer)","Do not Progress – module retriever","Do not Progress – module retriever","Do not Progress – module retriever","Do not Progress – module retriever","Do not Progress – module retriever","Do not Progress – module retriever","Do not Progress – module retriever","Do not Progress – module retriever","Do not Progress – module retriever","Do not Progress – module retriever","Do not Progress – module retriever","Exclude","Do not progress – module retriever","Do not progress – module retriever","Do not progress – module retriever","Do not progress – module retriever","Exclude","Exclude","Do not progress – module retriever","Do not progress – module retriever","Do not progress – module retriever","Do not progress – module retriever","Exclude","Exclude","Exclude"]     #list of possible outcome values
    while True:
        try:
            Pass_Credit=int(input("Please enter the number of credits at Pass: "))  #prompt for the number of credits for pass
            if Pass_Credit!=0 and Pass_Credit!=20 and Pass_Credit!=40 and Pass_Credit!=60 and Pass_Credit!=80 and Pass_Credit!=100 and Pass_Credit!=120:    #checks whether a valid credit is entered by the user.
                print ("Out of range\n")    #an error message is displayed
                continue
            Defer_Credit=int(input("Please enter the number of credits at Defer: "))    #prompt for the number of credits for defer
            if Defer_Credit!=0 and Defer_Credit!=20 and Defer_Credit!=40 and Defer_Credit!=60 and Defer_Credit!=80 and Defer_Credit!=100 and Defer_Credit!=120:    #checks whether a valid credit is entered by the user.
                print ("Out of range\n")    #an error message is displayed
                continue
            Fail_Credit=int(input("Please enter the number of credits at Fail: "))  #prompt for the number of credits for fail
            if Fail_Credit!=0 and Fail_Credit!=20 and Fail_Credit!=40 and Fail_Credit!=60 and Fail_Credit!=80 and Fail_Credit!=100 and Fail_Credit!=120:    #checks whether a valid credit is entered by the user.
                print ("Out of range\n")    #an error message is displayed
                continue
            Total=Pass_Credit+Defer_Credit+Fail_Credit  #gets the sum of all the credits entered (Pass, Defer, Fail)
            if Total>120 or Total<120: #the maximum amount of credits that can be obtained from Pass, Defer, Fail is 120
                print("Total incorrect\n")    #if the total number of credits is more than or less than 120 it is incorrect
                continue
        except ValueError:
            print("Integer required\n")  #asks the user to display an integer value
            continue
        break
    x=Pass.index(Pass_Credit)   #finds the location of the item in the Pass list
    y=Defer.index(Defer_Credit) #finds the location of the item in the Defer list
    z=Fail.index(Fail_Credit)   #finds the location of the item in the Fail list
    def outcomes():
        global Pass_Credit, Defer_Credit, Fail_Credit, Progress, Trailer, Retriever, Exclude 
        print(Outcome[x])
        if Outcome[x]=="Progress":   #checks whether the outcome(x) correponds to Progress
            Progress+=1     #the Progress counter is being incremented each time
            Progress_List.append([Pass_Credit,Defer_Credit,Fail_Credit])    #the values entered by the user (progress outcome) is being added into the end of a list (Progress_List) because it can be later used when reading and writing into text files
        if Outcome[x]=="Progress (module trailer)": #checks whether the outcome(x) correponds to Trailer
            Trailer+=1  #the Trailer counter is being incremented each time
            Trailer_List.append([Pass_Credit,Defer_Credit,Fail_Credit]) #the values entered by the user (trailer outcome) is being added into the end of a list (Trailer_List) because it can be later used when reading and writing into text files 
        if Outcome[x]=="Do not Progress – module retriever":    #checks whether the outcome(x) correponds to Retriever
            Retriever+=1    #the Retriever counter is being incremented each time
            Retriever_List.append([Pass_Credit,Defer_Credit,Fail_Credit])   #the values entered by the user (retriever outcome) is being added into the end of a list (Retriever_List) because it can be later used when reading and writing into text files
        if Outcome[x]=="Exclude":   #checks whether the outcome(x) correponds to Exclude
            Exclude+=1  #the Exclude counter is being incremented each time
            Exclude_List.append([Pass_Credit,Defer_Credit,Fail_Credit])   #the values entered by the user (exclude outcome) is being added into the end of a list (Exclude_List) because it can be later used when reading and writing into text files  
        while True:
             ID=input("Please enter the Student ID: ")   #asks the user to enter the ID
             if ID=="":     #if the user does not enter the ID
                  continue  #if the user does not enter the ID it will be asked again and again until the ID is entered 
             else:
                  break     #if the user has entered the ID then it breaks the loop
        StdID[ID]=[f"{Outcome[x]} - "+str(Pass_Credit)+","+str(Defer_Credit)+","+str(Fail_Credit)]  #corresponding outcome's dictionary
        return StdID
    if True:
        while True:
            y=x     #assigns the position of x to the position of y
            z=x     #assigns the position of x to the position of z
            if Defer[y]==Defer_Credit and Pass[x]==Pass_Credit and Fail[z]==Fail_Credit:    #checks whether the item in the assigned position is equal to the value entered by the user
                outcomes()
                break
            else:
                y+=1    #increments the position in the Defer list by 1
                x+=1    #increments the position in the Pass list by 1
                z+=1    #increments the position in the Fail list by 1
                continue    #after the incrementation it again iterates and checks whether the item in the list of the new position corresponds to the value entered by the user
    Next=input("\nWould you like to enter another set of data?\nEnter \'y\' for yes or \'q\' to quit and view the results:")
    Next=Next.lower()   #even if the user enters uppercase y or q it will be accepted (program autonatically converts to lowercase letters)
    def histogram():
        global Progress, Trailer, Retriever, Exclude
        print("-----------------------------------------------------------------------------")
        print("Histogram")
        print("Progress",Progress,"  : ",Progress*"*")
        print("Trailer",Trailer,"   : ",Trailer*"*")
        print("Retriever",Retriever," : ",Retriever*"*")
        print("Exclude",Exclude,"   : ",Exclude*"*")
        print(Progress+Trailer+Retriever+Exclude,"outcomes in total")
        print("-----------------------------------------------------------------------------")   
    if Next=="y":
        print("\n") #goes to the beginning of the program if the user enters y
        continue
    elif Next=="q": #terminates the loop and prints the histogram and the dictionary
        histogram()
    else:
        while True:
            Next=input("\nWould you like to enter another set of data?\nEnter \'y\' for yes or \'q\' to quit and view the results: ")
            Next=Next.lower()   
            if Next=="q":   
                histogram()
                break
            elif Next=="y":
                break
            else:
                Next!="y" or Next!="q"  #if the user does not enter y or q the program will run the loop an valid input is entered (y or q)
                continue
    if Next=="y":
        print("\n")
        continue
    f=open("file.txt","w")
    for i in range(len(Progress_List)):
        p=', '.join(str(List) for List in Progress_List[i]) #removes the brackets in the progress list
        f.write(str(f"Progress - {p}\n"))
    for i in range(len(Trailer_List)):
        t=', '.join(str(List) for List in Trailer_List[i])  #removes the brackets in the trailer list
        f.write(str(f"Progress (module trailer) - {t}\n"))
    for i in range(len(Retriever_List)):
        r=', '.join(str(List) for List in Retriever_List[i])   #removes the brackets in the retreiver list
        f.write(str(f"Do not Progress – module retriever - {r}\n"))
    for i in range(len(Exclude_List)):
        e=', '.join(str(List) for List in Exclude_List[i])  #removes the brackets in the exclude list
        f.write(str(f"Exclude - {e}\n"))
    f.close()
    f=open("file.txt","r")
    content=f.read()
    print(f"{content}\n")
    f.close()
    print(StdID)
    break
