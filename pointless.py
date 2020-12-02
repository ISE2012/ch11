def pointless(required_param, *args):
    print ('Required parameter:', required_param)
    if args:
        print("Other parameter/s: ", str(args))


pointless(1)
pointless(1, 2)
pointless(1, 2.0, 'three')
pointless(1, 2.0, 'three', [4])

