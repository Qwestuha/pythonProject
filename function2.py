def create_record(name , phone, address):
    """"Create Record"""
    record = {
        'name': name,
        'phone': phone,
        'address': address

    }
    return record


user1 = create_record("Vasya", "+324245235234523453452345235", "Tunussia")
user2 = create_record("Petya", "+32424234231453463457354673234", "Munisia")

print(user1)
print(user2)


def give_award(medal, *persons):
    """"Give Medals to persons"""
    for person in persons:
        print(" Tovarish " + person.title() + " награждается медалью " + medal)

give_award('ЗА Берлин', "vasya", "petya")
give_award('Za London', 'petya', 'alexander', 'valintin')

