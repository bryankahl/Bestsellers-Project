def yearrangefinder(line):
    linesyear = []
    #yearrange1 = open('bestsellers.txt', 'r')
    #yearrange1.readlines()
    yearrange = ''
    while type(yearrange) == str:
        try:
            yearrange = int(input("Enter a starting year:"))
        except ValueError:
            print("Invalid input, please try again\n")

    lastyear = yearrange - 1

    while lastyear < yearrange:
        try:
            lastyear = int(input("Enter a last year:"))
            if lastyear < yearrange:
                print("Last year must not be less than starting year, please try entering valid input.\n")
            else:
                pass
        except ValueError:
            print("Invalid input, please enter numeric data.\n")
            
        
    for x in range(yearrange, lastyear+1):
        something = str(x)
        for y in line:
            if something in y:
                y = y.rstrip('\n')
                y = y.split('\t')
                app = (f'{y[0]} by: {y[1]} (pub date: {y[3]})')
                linesyear.append(app)
                
    ##yearrange1.close()
    if linesyear == []:
        print("Your search returned an empty string")
    else:
        for x in linesyear:
            print(x)
if __name__ == '__main__':
    main()
