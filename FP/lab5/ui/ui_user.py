from domain.user_domain import User
from repository.user_repository import UserRepository
from service.service_user import Service_User
from domain.validation import Validation

def show_menu():
    print("\nUser Management Menu:")
    print("1. Show all users")
    print("2. Add a user")
    print("3. Remove a user")
    print("4. Update a user")
    print("5. Exit")

def show_all_users(Service_User):
    users = Service_User.get_users()
    if not users:
        print("No users available.")
    else:
        for user in users:
            print(f"ID:{user.user_id}, {user.name}, {user.age}")

def add_user(service_user):
    try:
        name = input("Enter user name: ")
        age = int(input("Enter user age: "))
        service_user.add_user(name, age)
        print("User added successfully!")
    except ValueError as e:
        print(f"Error: {e}")

def remove_user(service_user):
    try:
        user_id = int(input("Enter user ID to remove: "))
        service_user.remove_user(user_id)
        print("User removed successfully!")
    except ValueError as e:
        print(f"Error: {e}")

def update_user(service_user):
    try:
        user_id = int(input("Enter user ID to update: "))
        name = input("Enter new name: ")
        age = int(input("Enter new age: "))
        updated_user = User(user_id, name, age)
        service_user.update_user(updated_user)
        print("User updated successfully!")
    except ValueError as e:
        print(f"Error: {e}")

def user_menu():
    file_path = "users.txt"
    validator = Validation()
    user_repository = UserRepository(file_path)
    service_user = Service_User(validator, user_repository)

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            show_all_users(service_user)
        elif choice == "2":
            add_user(service_user)
        elif choice == "3":
            remove_user(service_user)
        elif choice == "4":
            update_user(service_user)
        elif choice == "5":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")