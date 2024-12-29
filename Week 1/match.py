name = input("What's your name ? ")

#if name == "harry"  or "hermonine" or "Ron":
    ##print ("Grii")
#elif name == "Draco":
    #print("sly")
#else:
    #print("Who?")

################################# match case

match name :
    case "Harry" | "Hermoine" | "Ron" :
        print ("Grii")
    case "Draco":
        print("Sly")
    case _ :
        print("who?")