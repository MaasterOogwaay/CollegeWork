class Node:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.next = None

    def printNode(self):
        return '[' + self.name + ':' + str(self.age) + ']-->'


class HashTable:

    def __init__(self):

        self.head = [None, None, None, None, None, None, None, None, None, None]

    def hash(self, key):
        return ord(key[0]) % 10

    def insert(self, name, age):
        index = self.hash(name)
        temp = Node(name, age)
        if self.head[index] == None:
            self.head[index] = temp
        else:
            temp.next = self.head[index]
            self.head[index] = temp

    def countOccurs(self, name):
        result = 0
        temp = self.head
        while temp != None:
            if temp.name == name:
                result += 1
            temp = temp.next

        return result

    def search(self, name):
        found = False
        index = self.hash(name)
        temp = self.head[index]
        while temp != None:
            if temp.name == name:
                found = True
            temp = temp.next

        return found

    def sumOfAllAges(self):
        result = 0
        temp = self.head
        while temp != None:
            result += temp.age
            temp = temp.next

        return result

    def oldest(self):
        result = 0
        temp = self.head
        while temp != None:
            if temp.age >= result:
                result = temp.age
            temp = temp.next
        return result

    def printList(self, index):
        result = 'Head ['+str(index)+']-->'
        temp = self.head[index]
        while temp != None:
            result += temp.printNode()
            temp = temp.next
        result += 'Null'
        return result
