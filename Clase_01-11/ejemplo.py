import random

def randint():
    return random.randint(1,100)

print(random.__name__)
print(__name__)
for i in range(3):
    a = randint()
    print(a)