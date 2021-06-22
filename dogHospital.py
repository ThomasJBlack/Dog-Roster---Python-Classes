from DogClass import Dog
from os import system
from switchFuncs import switch

print("clear me")
_ = system('clear')
print("\n\nnew run\n\n")

# initial 5 random dogs.
dogs = []
while len(dogs) < 5:
    dogs.append(Dog())
# print the names of the dogs
Dog.printNames(array=dogs)

choicePromts = [
    "\nPlease enter an integer to choose one of the following.",
    "(1) More info on a dog",
    "(2) Add a dog patient",
    "(3) Remove a dog patient",
    "(4) Edit a dog patient's information\n"
]

scriptInProgress = 1

while scriptInProgress:
    for prompt in choicePromts:
        print(prompt)

    choice = int(input("Choice int: "))
    # based on user's choice, this switch-equivalent function will call functions accordingly
    switch(choice, dogs)

    scriptInProgress = int(input("Enter a truthy number to continue: "))
