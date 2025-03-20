from domain.user_domain import User

class UserRepository:
    def __init__(self, file_path):
        self.users = []
        self.file_path = file_path
        self.__load()

    def __save(self):
        with open(self.file_path, "w") as file:
            for user in self.get_all():
                file.write(f"{user.user_id},{user.name},{user.age}\n")

    def __load(self):
        users = []
        try:
            with open(self.file_path, "r") as file:
                for line in file:
                    user_id, name, age = line.strip().split(",")
                    users.append(User(int(user_id), name, int(age)))
        except FileNotFoundError:
            pass
        self.users = users

    def get_all(self):
        return self.users

    def gen_id_user(self):
        return max([e.user_id for e in self.users], default=0) + 1

    def find(self, user_id):
        result = list(filter(lambda user: user.user_id == user_id, self.users))
        return self.users.index(result[0]) if result else -1


    def add(self, user: User):
        if self.find(user.user_id) != -1:
            raise ValueError("This user exists already!")
        self.users.append(user)
        self.__save()

    def update(self, userupdated: User):
        pos = self.find(userupdated.user_id)
        if pos == -1:
            raise ValueError("The user with the given id doesn't exist!")
        self.users[pos] = userupdated
        self.__save()

    def delete(self, iduser: int):
        pos = self.find(iduser)
        if pos == -1:
            raise ValueError("The user with the given id doesn't exist!")
        del self.users[pos]
        self.__save()