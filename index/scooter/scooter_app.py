from scooter_item import ScooterItem
from scooter_user import ScooterUser

class ScooterApp:
    def __init__(self):
        self.stations = {
            'London': [],
            'Cambridge': [],
            'Liverpool': [],
        }
        self.registered_users = {}

    def register_user(self, username, password, age):
        if username in self.registered_users:
            raise ValueError("Username taken")
        elif age < 18:
            raise ValueError("Below 18")
        else:
            new_user = ScooterUser(username, password, age)
            self.registered_users[username] = new_user
            print("Account created for " + username)

    def login_user(self, username, password):
        user = self.registered_users.get(username)
        if user:
            user.login(password)
        else:
            raise ValueError("User not found")

    def logout_user(self, username):
        user = self.registered_users.get(username)
        if user:
            user.logout()
        else:
            raise ValueError("User not found")

    def create_scooter(self, station):
        if station not in self.stations:
            raise ValueError("Invalid station")
        else:
            new_scooter = ScooterItem(station)
            print("Scooter " + str(new_scooter.serial) + " created")

    def dock_scooter(self, scooter, station):
        scooter.dock(station)
        self.stations[station].append(scooter)

    def rent_scooter(self, scooter, user):
        scooter.rent(user)

    def print_info(self):
        print(self.stations)
        print(self.registered_users)


# These object declarations are used to demonstrate the scooter functionality
user1 = ScooterUser("Caydn", "password", 18)
scooter1 = ScooterItem("Cambridge")
user2 = ScooterUser("Not Caydn", "passw0rd", 21)
scooter2 = ScooterItem("Cambridge")

# These print statements are not efficient but they are used to show the line separation between objects in the console!
print(user1)
print("")
print(scooter1)
print("")
user1.login("password")
print("")
print(user1)
print("")
scooter1.rent(user1)
print("")
print(scooter1)
print("")
print(user2)
print("")
print(scooter2)