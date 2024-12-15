class User:
    def __init__(self,username,email):
        self.username = username
        self.email = email

    def display_info(self):
        return f'User: {self.username}, Email: {self.email}'

    def __str__(self):
        return self.display_info()

class Admin(User):
    def __init__(self, username, email, permissions):
        #jesli nadpisujemy init to musimy wowolac init metoda tez z ktorej klasy dziedziczymy
        super().__init__(username,email)
        self.permissions = permissions

    def display_info(self):
        return f'Admin : {self.username}, Permissions: {self.permissions}'

admin = Admin('karo', 'karoszym@interia.pl', ['delete_user', "create_user"])
print(admin)
print(isinstance(admin, Admin)) # ze admin jest adminem
print(isinstance(admin, User)) #ze admin ma wlasciwosci usera - True

