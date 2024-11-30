from abc import ABC
class Animal(ABC):
    def move (self):
        pass
class human(Animal):
    def move (self):
        return "I can move"
    
class snake(Animal):
    def move(self):
        return "I can crawl"
    
class dog(Animal):
    def move(self):
        return "I can bark"
class lion(Animal):
    def move(self):
        return "I can roar"


h=human()
print(h.move())

s=snake()
print(s.move())

l=lion()
print(l.move())
d=dog()
print(d.move())



