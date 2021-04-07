class Node:
    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age
        self.next = None

#To input name and age of 10 person
class SLinkedList:
    def __init__(self):
        self.headval = None


X = SLinkedList()
X.headval = Node(input("Name"), input("Age"))
Start = X.headval
for i in range(9):
    X.headval.next = Node(input("Name"), input("Age"))
    X.headval = X.headval.next

X.headval = Start

while X.headval is not None:
    print(X.headval.name + " " + X.headval.age)
    X.headval = X.headval.next

