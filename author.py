def authorfinder(line):
    listauthorname = []
    ##authorfind = open('bestsellers.txt', 'r')
    ##line = authorfind.readlines()
    authorname = input("Enter an author name: ")
    try:
        while type(int(authorname)) == int:
                print("You only entered numeric data, please try again.\n")
                authorname = input("Enter an author name: ")
    except ValueError:
        pass
        
             
    for x in line:
        z = x.split('\t')
        if authorname.casefold() in z[1].casefold():
            y = x.rstrip('\n')
            y = y.split('\t')
            app = (f'{y[0]} by: {y[1]} (pub date: {y[3]})')
            listauthorname.append(app)
    ##authorfind.close()

    if listauthorname == []:
        print("Your search returned an empty string")
    else:
        for x in listauthorname:
            print(x)
if __name__ == '__main__':
    main()
