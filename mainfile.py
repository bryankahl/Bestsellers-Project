import author
import title
import yearrange
import yearmonth
def main():
    totallines = 0 
    filereader = open('bestsellers.txt', 'r')
    lines = filereader.readlines()
    for x in lines:
        totallines+=1
    print(f"Read {totallines} books.")

    choice = ''
    while choice.upper() != 'Q':
        choice = input("What would you like to do?\n\t1: Look up year range\n\t2: Look up month/year\n\t3: Look up author\n\t4: Search for title\n\tQ: Quit\n\t")
        if choice == '1':
            yearrange.yearrangefinder(lines)
        elif choice == '2':
            yearmonth.monthyearfinder(lines)
        elif choice == '3':
            author.authorfinder(lines)
        elif choice == '4':
            title.titlefinder(lines)
        elif choice.upper() == 'Q':
            print("Done")
        else:
            print("I dont understand this command")

    filereader.close()




    
if __name__ == '__main__':
    main()

