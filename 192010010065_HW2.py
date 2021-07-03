from datetime import date


def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    print("Enter Year:", year)

    return False

while True:
    year = int(input("Enter Year: Press 0 to exit."))


    if year == 0:
        break

    else:
        year = int(year)

        if is_leap_year(year):

            print(year, "Leap Year. Enter Another Year:")
        else:
            if date(year, 2, 1).strftime('%A') == 'Monday':
                print("Year Perfect February:", year)
                count = 1
                for sayi in range(10, year):
                    if ((not(sayi % 4 == 0 and sayi % 100 != 0) or (sayi % 400 == 0)) and (date(sayi, 2, 1).strftime('%A') == 'Monday') and sayi < year ):

                        print("These years include the perfect February:", sayi)
                        count = count + 1
                print("Total number of years:" + str(count))


            elif date(year, 2,1).strftime("%A") != 'Monday':
                print("Year,does not include Perfect February:",year)



    print("""///////////////////////////////////////////
    HASAN KAAN KAHRAMAN
    192010010065
///////////////////////////////////////////""")













