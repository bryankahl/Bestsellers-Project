def monthyearfinder(line):
    listmonthyears = []
    ##yearmonth = open('bestsellers.txt', 'r')
    ##line = yearmonth.readlines()
    month = -1
    year = '-1'
    while month not in range(1, 13):
        try:
            month = int(input("Enter a month (xx): "))
            if month not in range(1, 13):
                print("Invalid input, try again.\n")
            else:
                pass
        except ValueError:
            month = -1
            print("Invalid input, try again.\n")
            
    month = '\t' + str(month) + '/'
    
    while type(year) == str:
        try:
            year = int(input("Enter a year (xxxx): "))  
        except ValueError:
            year = '-1'
            print("Invalid input, enter numeric data")
            
    for x in line:
        if str(month) in x and str(year) in x:
            y = x.rstrip('\n')
            y = y.split('\t')
            app = (f'{y[0]} by: {y[1]} (pub date: {y[3]})')
            listmonthyears.append(app)
    ##yearmonth.close()
    if listmonthyears == []:
        print("Your search returned an empty string")
    else:
        for x in listmonthyears:
            print(x)

if __name__ == '__main__':
    main()
