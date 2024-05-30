from Employee import Employee
from OrgIterator import OrgIterator

class Organization:
    def __init__(self, root: Employee):
        self.root = root

    def __iter__(self):
        return OrgIterator(self.root)
