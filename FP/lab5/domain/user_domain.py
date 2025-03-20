class User:
    def __init__(self, user_id, name, age):
        self._user_id = user_id
        self._name = name
        self._age = age

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value

    def __str__(self):
        return f"User[ID={self.user_id}, Name={self.name}, Age={self.age}]"