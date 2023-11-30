class ScooterUser:
    def __str__(self):
        return f"User Name:\n{self.username}\nUser Age:\n{self.age}\nUser Login:\n{self.logged_in}"

    def __init__(self, username, password, age):
        self.username = username
        self.password = password
        self.age = age
        self.logged_in = False

    def login(self, password):
        if password == self.password:
            self.logged_in = True
            print("Login success")
        else:
            self.logged_in = False
            raise ValueError("Login failure")

    def logout(self):
        self.logged_in = False
        print("Logout Success")