def printall(*args):
    print(args)
    if(len(args)>1):
        print("second args: "+str(args[1]))

printall(1)
printall(1, 2.0)
printall(1, 2.0, 'three')

