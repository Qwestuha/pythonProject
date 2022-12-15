import re

mytext= "Vasya aaaaaaaaaaaaaaaaaaaa 1972, Kolya - 1972: Olesya 1981, aaaaaaaaa@intel.com
        "bbbbbbbbbbbbbb@intel.com, Petya gggggggggg, 1992,cccccccccccc@yahoo.com,"
        "ddddddddddddd@intel.com, vasya@yandex.net, hello hello, Misha $43 1984, Vladimir 1977, Irina, 2001, annnnn@intel.com, eeeeeeeeeee@yandex.com, oooooooo"


textlookfor = r"yandex.ru"
allresults = re.findall(textlookfor, mytext)

print(allresults)