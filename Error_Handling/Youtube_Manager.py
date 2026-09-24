
def list_all_vadios(vadios):
    pass

while true:
    print("\n Youtube Manager | choose an option ")
    print("1. List all youtube vadio ")
    print("2. Add a youtube vadio ")
    print("3. update youtube vadio details ")
    print("4. Delete a youtube vadio ")
    print("5. Exit the app")
    choose = input("Enter your choice ")

    match choice:
        case '1':
            list_all_vadios(vadio)