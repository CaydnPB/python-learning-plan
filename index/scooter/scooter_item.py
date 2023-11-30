class ScooterItem:
    next_serial = 1

    def __str__(self):
        return f"Serial Number:\n{self.serial}\nScooter Station:\n{self.station}\nScooter User:\n{self.user}\nScooter Charge:\n{self.charge}"

    def __init__(self, station):
        self.station = station
        self.user = None
        self.serial = ScooterItem.next_serial
        ScooterItem.next_serial += 1
        self.charge = 100
        self.is_broken = False

    def rent(self, user):
        if not self.is_broken and self.charge > 20:
            self.user = user
            print("Scooter rented by " + user.username)
        elif self.charge <= 20:
            raise ValueError("Scooter cannot be rented due to low charge")
        else:
            raise ValueError("Scooter cannot be rented due to being broken")

    def dock(self, station):
        valid_stations = {"London", "Cambridge", "Liverpool"}
        if station not in valid_stations:
            raise ValueError("Invalid station")
        else:
            self.station = station
            self.user = None
            print("Scooter docked at " + station)

    # def recharge(self):
        # Implementation for recharging

    # def request_repair(self):
        # Implementation for requesting repair