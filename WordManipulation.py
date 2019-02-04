while True:
    stringVal = input("Input a word: ")
    #stringVal = "Dinerificio" #used for manual testing
    stringLength = len(stringVal)
    print()
    print("|||Details|||")
    print()
    print(stringVal)
    print(stringLength,"characters")
    if stringLength%2==0:
        print("Even character length")
    else:
        print("Odd character length")
    print()
    print("|||Functions|||")
    print()
    def BuildStringUpDown():
        print("- Build Up & Down")
        a=1;
        while a <=stringLength:
            print(stringVal[:a])
            a+=1;
        a=1;
        while a <stringLength:
            print(stringVal[:-a])
            a+=1;
        print("-----")

    def EmergeString():
        print("- Emerge")
        a=1;
        if stringLength%2==0:
            while a <=(stringLength//2):
                print(stringVal[:a]+stringVal[-a:])
                a+=1;
        if stringLength%2==1:
            while a <=((stringLength+1)//2):
                print(stringVal[:a-1]+stringVal[-a:])
                a+=1;
        print("-----")


    def SplitCombineString():
        print("- Split Combine")
        a=1;
        if stringLength%2==0:
            while a <=((stringLength//2)):
                print(stringVal[:a]+""+stringVal[stringLength//2:(stringLength//2)+a])
                a+=1;
        if stringLength%2==1:
            while a <=((stringLength+1)//2):
                print(stringVal[:a-1]+""+stringVal[stringLength//2:(stringLength//2)+a])
                a+=1;
        print("-----")

    def ReverseString():
        print("- Reverse")
        reversedStringVal=stringVal
        stringArray=[]
        stringArray.append(reversedStringVal[stringLength-1])
        for i in range(stringLength):
            if i>0:
                stringArray.append(stringVal[-i-1:-i])
        reversedStringVal = ''.join(stringArray)
        print(reversedStringVal)
        print(reversedStringVal.title())
        print("-----")

    BuildStringUpDown()
    EmergeString()
    SplitCombineString()
    ReverseString()



    continueInput= input('y to start again or n to exit: ')
    #print(continueInput)
    if continueInput=='y':
        continue
    elif continueInput=='n':
        break
    else:
        break
