altitude = int(input("Enter the altitude of plane: "))
if altitude <= 1000 :
    print('Safe to Land')
elif 1000 < altitude <= 5000 :
    print('Bring down to 1000 ft')
elif altitude > 5000 :
    print('Turn Around and Try Later')
