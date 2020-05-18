from doctor import Doctor


class Private(Doctor):
    def __init__(self, dname, title, patient, treatmentFee):
        super().__init__(dname, title)
        self.__treatmentFee = treatmentFee
        self.__patient = patient

    def __calculate_payment(self):
        return self.__treatmentFee * self.__patient

    def __repr__(self):
        return self.getTitle() + ' - ' + self.getDname() + " Payment: " + str(self.__calculate_payment())

