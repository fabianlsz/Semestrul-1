user_file = "C:/Users/Fabian/Desktop/FP/lab3/users.txt"

#######################################################################################################
#                           '"user_file = users.txt ----- nu merge???"'                               #
#######################################################################################################


def load_users():
    """Functia incarca lista de utilizatori users.txt

    Returns
    -------
    list
        Lista de dictionare cu utilizatori
    """
    users = []
    try:
        with open(user_file, "r") as file:
            for line in file:
                name, age = line.strip().split(",")
                users.append({"name": name, "age": int(age)})
    except FileNotFoundError:
        print("File not found")
    return users


def save_user(users):
    """Functia salveaza utilizatorii in lista users.txt

    Parameters
    ----------
    users : list
        Lista de dictionare cu utilizatori
    """
    with open(user_file, "w") as file:
        for user in users:
            file.write(f"{user['name']},{user['age']}\n")


def add_user(users, name, age):
    """Functia adauga utilizatori in lista de dictionare

    Parameters
    ----------
    users : list
        Lista de dictionare cu utilizatori
    name : string
        Numele utilizatorului care va fi adaugat in lista de dictionare
    age : int
        Varsta utilizatorului care va fi adaugata in lista de dictionare
    """
    with open(user_file, "w") as file:
        users.append({"name": name, "age": age})
        save_user(users)


def delete_user(users, name):
    """Functia sterge un utilizator in lista de dictionare users.txt

    Parameters
    ----------
    users : list
        Lista de dictionare cu utilizatori
    name : string
        Numele utilizatorului care va fi sters din lista de dictionare

    Returns
    -------
    list
        Lista de dictionare actualizata dupa stergerea utilizatorului
    """
    user_found = False
    for i in range(len(users)):
        if users[i]["name"] == name:
            del users[i]
            user_found = True
            save_user(users)
            break
    return user_found


def update_user(users, name, new_name, new_age):
    user_found = False
    for user in users:
        if user["name"] == name:
            if new_name:
                user["name"] = new_name
            if new_age:
                user["age"] = new_age
            user_found = True
            break
    return user_found