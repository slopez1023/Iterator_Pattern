class Employee:
    def __init__(self, name: str, position: str):
        self.name = name
        self.position = position
        self.subordinates = []

    def add_subordinate(self, subordinate: 'Employee'):
        self.subordinates.append(subordinate)

    def __str__(self):
        return f'{self.position}: {self.name}'