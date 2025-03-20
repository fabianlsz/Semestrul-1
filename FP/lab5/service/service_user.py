from domain.validation import Validation
from domain.user_domain import User
from repository.user_repository import UserRepository


class Service_User:
    def __init__(self, validator: Validation, repoUser: UserRepository):
        self.Validator = validator
        self.UserRepository = repoUser

    def add_user(self, name: str, age: int):
        for user in self.UserRepository.get_all():
            if user.name == name and user.age == age:
                raise ValueError("Utilizatorul exista deja!")
        idUserNou = self.UserRepository.gen_id_user()
        userNou = User(idUserNou, name, age)
        self.Validator.validator_user(userNou)
        self.UserRepository.add(userNou)
    def remove_user(self, iduser: int):
        self.UserRepository.delete(iduser)

    def update_user(self, iduser):
        self.UserRepository.update(iduser)

    def get_users(self):
        return self.UserRepository.get_all()