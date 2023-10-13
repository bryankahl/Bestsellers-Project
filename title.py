def titlefinder(line):
    listtitles = []
    ##titlefind = open('bestsellers.txt', 'r')
    ##line = titlefind.readlines()
    titlename = input("Enter a book title: ")
    
    for x in line:
        z = x.split('\t')
        if titlename.casefold() in z[0].casefold():
            y = x.rstrip('\n')
            y = y.split('\t')
            
            app = (f'{y[0]} by: {y[1]} (pub date: {y[3]})')
            listtitles.append(app)
     ##titlefind.close()
    if len(listtitles) is 0:
        print("Your search returned an empty string")
    else:
        for x in listtitles:
            print(x)
if __name__ == '__main__':
    main()
