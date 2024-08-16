def get_full_name(first_name :str, last_name:str):
    full_name = first_name.title() + " " + last_name.title()
    return full_name


print(get_full_name("john", "doe"))


from enum import Enum

# class syntax

class color(Enum):

    RED = 1

    GREEN = 2

    BLUE = 3

# functional syntax

print (color.RED.name, color.GREEN.value, list(color))




import enum
class Animal(enum.Enum):
    dog = 1
    cat = 2
    lion = 3
di = {}
di[Animal.dog] = 'bark'
di[Animal.lion] = 'roar'
print(di[Animal.dog])
if di == {Animal.dog: 'bark', Animal.lion: 'roar'}:
    print("Enum is hashed")
else:
    print("Enum is not hashed")