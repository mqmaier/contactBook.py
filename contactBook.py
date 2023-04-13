
contact = {}

##funcao mostrar contato
def display_contact():
    print("Name\t\tContact Number")
    for key in contact:
        print("{}\t\t{}".format(key,contact.get(key)))
while True: ##loop opcoes
    choice = int (input(" 1. New contact \n 2. Search contact \n 3. Show contacts \n 4. Edit contact \n 5. Delete contact \n 6. Exit \n Enter a option"))
    if choice == 1: ##1 criar novos contatos, falta corrigir formato de tel
        name = input("Enter the contact name: ")
        phone = input("Enter the cellphone number: ")
        contact[name] = phone
    elif choice == 2: 
        search_name = input("Enter the contact name: ")
        if search_name in contact:
            print(search_name,"'s contact number is: ",contact[search_name])
        else:
            print ("Contact is not found")
    elif choice == 3: ## mostrar contatos enumerados
        if not contact:
            print ("empty contact book")
        else:
            display_contact()
    elif choice == 4: 
        edit_contact = input("Enter the contact to be edited ")
        if edit_contact in contact:
            phone = input("Enter the cellphone number: ")
            contact[edit_contact]=phone
            print("Contact updated")
            display_contact()
        else:
            print("Contact is not found")
    elif choice == 5: 
        del_contact = input("Enter the contact to be deleted")
        if del_contact in contact:
            confirm = input("Do you want to delete this contact y/n?")
            if confirm =='y' or confirm == 'Y':
                contact.pop(del_contact)
            display_contact()
        else:
            print("Contact is not found")
    else: 
        break









