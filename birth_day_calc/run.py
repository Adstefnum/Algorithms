from functions import main

#getting input
year = int(input("Year in full:"))
month = input("Pick a month no:\n1 = Jan\n 2 = Feb\n 3 = Mar\n 4 = Apr\n 5 = Mar\n 6 = Jun\n 7 = Jul\n 8 = Aug\n 9 = Sep\n 10 = Oct\n 11 = Nov\n 12 = Dec:")
day = int(input("Day:"))

print(main(year,month,day))

