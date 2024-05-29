#!/usr/bin/env python3

class Dog:
    def __init__(self, name, breed="Mutt"):
        self.name = name
        self.breed = breed

mbwa_kali = Dog("Simba")
print(mbwa_kali.name)

mbwa_kali.name = "Rex"
print(mbwa_kali.name)

mbwa_kali.breed = "German Shepherd"
print(mbwa_kali.breed)