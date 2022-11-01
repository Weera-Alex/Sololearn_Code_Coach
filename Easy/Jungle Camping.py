animal_sound = {
    "Rawr": "Tiger",
    "Grr": "Lion",
    "Ssss": "Snake",
    "Chirp": "Bird",
}

sounds = input().split()
for x in sounds:
    print(animal_sound[x], end=" ")
