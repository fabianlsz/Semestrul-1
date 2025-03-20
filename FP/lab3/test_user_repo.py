from user_repositories import load_users, save_user, add_user, delete_user, update_user


def test_add_user():
    original_users = load_users()

    try:
        test_users = original_users.copy()

        test_name = "Alina"
        test_age = 25

        add_user(test_users, test_name, test_age)

        assert any(
            user["name"] == test_name and user["age"] == test_age for user in test_users
        ), "Utilizatorul va fi adaugat."

    finally:
        save_user(original_users)
        print("Users file restored.")


def test_delete_user():
    original_users = load_users()

    try:
        test_users = original_users.copy()

        test_name = "Mihai"
        test_age = 30
        add_user(test_users, test_name, test_age)

        deleted = delete_user(test_users, test_name)

        assert deleted == True, "Utilizatorul va fi sters."
        assert not any(
            user["name"] == test_name for user in test_users
        ), "Utilizatorul nu se mai afla in lista."

    finally:
        save_user(original_users)
        print("Users file restored.")


def test_update_user():
    original_users = load_users()

    try:
        test_users = original_users.copy()

        initial_name = "Sincariul"
        initial_age = 40
        add_user(test_users, initial_name, initial_age)

        new_name = "Sincariu"
        new_age = 45
        update_user(test_users, initial_name, new_name, new_age)

        assert any(
            user["name"] == new_name and user["age"] == new_age for user in test_users
        ), "Utilizatorul va fi actualizat."

    finally:
        save_user(original_users)
        print("Users file restored.")


test_add_user()
test_delete_user()
test_update_user()

print("Toate testele au fost trecute cu succes!")