class Journal:
    def __init__(self) -> None:
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f"{self.count}: {text}")

    def remove_entry(self, pos):
        del self.entries[pos-1]

    def __str__(self):
        return "\n".join(self.entries)

class SaveFiles:
    @staticmethod
    def save_to_file(journal, filename):
        with open(file=filename, mode="w") as file:
            file.write(journal.__str__())

class LoadFiles:
    @staticmethod
    def load_from_file(filename):
        with open(file=filename, mode="r") as file:
            data = file.readlines()
            return data



j = Journal()
print(LoadFiles.load_from_file("Journal.txt"))



