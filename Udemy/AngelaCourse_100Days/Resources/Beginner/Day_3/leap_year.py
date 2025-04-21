#kazdy rok, który jest podzieny przez 4 
#każdy rok który jest niepodzielny przez 100, chyba ze jest podzielny przez 400

year = int(input("wpisz rok, który chcesz zweryfikować: "))

year_d4 = year/4
year_d100 = year/100
year_d400 = year/400

if year_d4 == int(year_d4):
    if year_d100 != int(year_d100):
            print("Ten rok jest rokiem przestępnym...")
    elif year_d100 == int(year_d100):
            if year_d400 == int(year_d400):
                print("Ten rok jest rokiem przestępnym...")
else:
    print("Ten rok nie jest rokiem przestępnym...")