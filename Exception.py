filename = "Lesson_List.txt"

try:
    myfile = open(filename, mode='r', encoding="Latin-1")
except Exception:
    print('Inside EXCEPT')
    print("Error Found!")
else:
    print("Indise ELSE")
    print(myfile.read())
finally:
    print("Inside FINALLY")



print(""""""""""""""""""""""EOF""""")