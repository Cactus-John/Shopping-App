
class Customers:
    def __init__(self, ID, First_name, Last_name, Pay):
        self.ID = ID
        self.First_name = First_name
        self.Last_name = Last_name
        self.Pay = Pay

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.First_name, self.Last_name)

    @property
    def fullname(self):
        return '{} {}'.format(self.First_name, self.Last_name, self.Pay)

    def __repr__(self):
        return "Customer('{}', '{}, {})".format(self.First_name, self.Last_name, self.Pay)
