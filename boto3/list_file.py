import os


for root, dir, file in os.walk(".", topdown=False):
    for name in file:
        print(os.path.join(name))
