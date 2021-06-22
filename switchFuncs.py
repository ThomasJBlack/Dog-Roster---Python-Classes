from DogClass import Dog


def switch(choice, dogs):
    return switchCases.get(choice, default)(dogs)


def print_info(dogs):
    Dog.printNames(array=dogs)
    dogIndex = int(input("Enter an integer for the dog you want to inspect: ")) - 1
    return dogs[dogIndex].printInfo()


def add_dog(dogs):
    return Dog.addDog(dogs)


def remove_dog(dogs):
    Dog.printNames(array=dogs)
    dogIndex = int(input("Enter an integer for the dog you want to remove: ")) - 1
    del dogs[dogIndex]


def edit_dog(dogs):
    Dog.printNames(array=dogs)
    dogIndex = int(input("Enter an integer for the dog you want to edit: ")) - 1
    dogs[dogIndex].editDog()


def default(dogs):
    return Dog.default()


switchCases = {
    1: print_info,
    2: add_dog,
    3: remove_dog,
    4: edit_dog,
    5: default
    }
