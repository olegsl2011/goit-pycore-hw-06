from Phone import Phone
from Name import Name

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

    def add_phone(self, number: str):
        self.phones.append(Phone(number))
        
    def remove_phone(self, number: str):
        self.phones = list(filter(lambda phone: phone == number,self.phones))
        
    def edit_phone(self, old_number, new_number):
        self.phones = list(map(lambda phone: Phone(new_number) if phone.value == old_number else phone, self.phones))
        
    def find_phone(self, number):
        for phone in self.phones:
            if phone.value == number:
                return phone
