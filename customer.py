class Customer:
    def __init__(self, name, contact):
        self.name = name
        self._contact = contact

    @property
    def contact(self):
        return self._contact

    @contact.setter
    def contact(self, new):
        self._contact = new

    @contact.deleter
    def contact(self):
        del self.contact
    def __str__(self):
        return f'{self.name}'
