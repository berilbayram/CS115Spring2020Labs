from doctor import Doctor


class State(Doctor):
    baseBonus = 5000

    def __init__(self, dname, title, salary):
        super().__init__(dname, title)
        self.__salary = salary

    def calculate_payment(self):
        if self.getTitle() == "Professor":
            return str(self.__salary + State.baseBonus * 125 / 100)
        elif self.getTitle() == "Associate Professor":
            return str(self.__salary + State.baseBonus)
        else:
            return str(self.__salary + State.baseBonus * 75 / 100)

    def __repr__(self):
        return self.getTitle() + " - " + self.getDname() + " Payment: " + self.calculate_payment()