# List of all names
from operator import le


names_list = []

# Load all names
with open("./Input/Names/invited_names.txt") as f:
    for name in f.readlines():
        name = name.replace("\n", "")
        names_list.append(name)


# Get Sample letter data
letter = ""
with open("./Input/Letters/starting_letter.txt") as f:
    letter = f.read()

# Generate letters for everyone
for name in names_list:
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", "w+") as f:
        content = letter.replace("[name]", name)
        f.write(content)

