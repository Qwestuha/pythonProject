#x = 25

#if x == 25:
 #   print("Yes you Right")
#else:
  #  print("No you are wrong!")

age = 18

if (age) <= 4:
   print("You are baby")
elif (age > 4) and (age < 12):
    print("You age kid")
elif (age >= 12) and (age < 19):
    print("You age teenager")
else:
    print("You are old")

print('------END-----')

all_cars = ['chrusler',  'dacia' ,'bmw', 'Kia' , 'vw' ,'seat', 'skoda' , 'lada', ' audi ' , 'ford' , ' Chevrolet' ]
german_cars = ['bmw', 'vw' , 'audi']

for xxxx in all_cars:
    if xxxx in german_cars:
        print(xxxx + " is German car")
    else:
        print(xxxx + " is not German car")
