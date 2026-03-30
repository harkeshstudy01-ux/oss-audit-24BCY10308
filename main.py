from password_tool import generate_password, check_strength
from integrity_checker import store, verify
from url_detector import check_url

def menu():

    while True:

        print("\nCyberSafe Toolkit")
        print("1 Generate Password")
        print("2 Check Password Strength")
        print("3 Store File Hash")
        print("4 Verify File")
        print("5 Check URL")
        print("6 Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            length = int(input("Length: "))
            print(generate_password(length))

        elif choice == "2":
            p = input("Enter password: ")
            print(check_strength(p))

        elif choice == "3":
            path = input("File path: ")
            print("Stored" if store(path) else "Error")

        elif choice == "4":
            path = input("File path: ")
            print(verify(path))

        elif choice == "5":
            url = input("Enter URL: ")
            print(check_url(url))

        elif choice == "6":
            break

menu()