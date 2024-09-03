#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self,name='dog',breed='breed'):
        self.name = name
        self.breed = breed
    def get_name(self):
        return self._name
    def set_name(self,name):
        if isinstance(name, str) and 1 <= len(name) <= 25:
        #and name.replace(" ","").isalpha():
            self._name = name.title()
        else:
            print("Name must be string between 1 and 25 characters.")
            self._name = 'dog'
    def get_breed(self):
        return self._breed
    def set_breed(self,breed):
        if breed in APPROVED_BREEDS or breed == 'breed' :
            self._breed = breed
        else:
            # add = ', '.join(APPROVED_BREEDS)
            print("Breed must be in list of approved breeds.")
            self._breed ='breed'

    name =property(get_name,set_name)
    breed = property(get_breed,set_breed)

