class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    def __lt__(self, other):
        return self.age < other.age

    def __gt__(self, other):
        return self.age > other.age

    def __le__(self, other):
        return self.age <= other.age

    def __ge__(self, other):
        return self.age >= other.age

    def __ne__(self, other):
        return self.age != other.age

p1 = Person("Alice", 25)
p2 = Person("Bob", 30)
p3 = Person("Alice", 25)

print(p1 == p2) 
print(p1 == p3) 
print(p1 < p2) 
print(p1 > p2) 