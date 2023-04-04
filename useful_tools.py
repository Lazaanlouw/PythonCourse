import random
feet_in_mile = 5280
meters_in_kilometer = 100
migos_gang = ["Quavo", "Takeoff", "Offset"]

def fet_file_ext(filename):
    return filename[filename.index(".") + 1]

def roll_dice(num):
    return random.randint(1, num)
