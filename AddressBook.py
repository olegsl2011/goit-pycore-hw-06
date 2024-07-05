from collections import UserDict

class AddressBook(UserDict):
    def add_record(self, record):

        if record.name.value in self.data:
            raise KeyError(f"Record with name '{record.name.value}' already exists.")
        self.data[record.name.value] = record
            
    def find(self, name):
        
        if name in self.data:
            return self.data[name]
        else:
            raise KeyError(f"Record with name '{name}' not found.")
        
    def delete(self, name):
        del self.data[name]
