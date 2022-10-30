import random

with open("./hyakunin.txt", encoding="utf-8") as f:
    wakas = [s.strip() for s in f.readlines()]

print("today's ikku" + wakas[random.randrange(len(wakas))])