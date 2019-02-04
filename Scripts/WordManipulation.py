def build_string_up_down(string="NULL"):
    """Prints the input string from char[0] to char[max].
    Then does the reverse."""

    print("- Build Up & Down")
    length = len(string)
    #Build up loop
    a = 1;
    while a <=length:
        print(string[:a])
        a +=1;
    #Build down loop
    a = 1;
    while a <length:
        print(string[:-a])
        a +=1;

    print("-" * 5)
    pass

def emerge_string(string="NULL"):
    """Grabs two sections of the string and prints their combination.
    Repeats until the full string is printed."""

    print("- Emerge")
    length = len(string)
    a = 1;
    #If the string is of an odd length, use length+1 and a-1 when running
    if length%2 == 0:
        while a <=(length//2):
            print(string[:a] + string[-a:])
            a +=1;
    if length%2 == 1:
        while a <=((length+1)//2):
            print(string[:a-1] + string[-a:])
            a +=1;

    print("-" * 5)
    pass

def split_combine_string(string="NULL"):
    """Splits the string in half and builds up each half.
    Prints each combination until the full string is printed."""

    print("- Split Combine")
    length = len(string)
    a = 1;
    #If the string is of an odd length, use length+1 and a-1 when running
    if length%2 == 0:
        while a <=((length//2)):
            print(string[:a] + "" + string[length//2:(length//2)+a])
            a +=1;
    if length%2 == 1:
        while a <=((length+1)//2):
            print(string[:a-1] + "" + string[length//2:(length//2)+a])
            a +=1;

    print("-" * 5)
    pass

def reverse_string(string="NULL"):
    """Prints the string in reverse, then capitalizes it."""

    print("- Reverse")
    length = len(string)
    #Store the characters in the string in an array so they can be rearranged
    reversedString=string
    stringArray=[]
    stringArray.append(reversedString[length-1])
    for i in range(length):
        if i > 0:
            stringArray.append(string[-i-1:-i])
    reversedString = ''.join(stringArray)
    print(reversedString)
    print(reversedString.title())

    print("-" * 5)
    pass

#Main script loop
while True:
    stringVal = input("Input a word: ")
    #used for manual, non-input testing
    #stringVal = "Test Value" 
    stringLength = len(stringVal)

    print()
    print("|||Details|||")
    print()
    print(stringVal)
    print(stringLength,"characters")
    if stringLength%2 == 0:
        print("Even character length")
    else:
        print("Odd character length")

    print()
    print("|||Functions|||")
    print()
    build_string_up_down(stringVal)
    emerge_string(stringVal)
    split_combine_string(stringVal)
    reverse_string(stringVal)

    continueInput= input("Input 'Y' to start again or 'N' to exit:")
    if continueInput == 'y' or continueInput == 'Y':
        continue
    elif continueInput == 'n' or continueInput == 'N':
        break
    else:
        break
