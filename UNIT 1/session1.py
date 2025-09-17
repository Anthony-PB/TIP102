# Breakout Problems Session 1
# Problem Set 1:
def welcome():
	print("Welcome to The Hundred Acre Wood!")

def greeting(name):
	print("Welcome to The Hundred Acre Wood " + name + "! My name is Christopher Robin.")

def print_catchphrase(character):
	if character == "Pooh":
        print("Oh bother!")
    else if character == "Tigger":
        print("TTFN: Ta-ta for now!")
    else ifcharacter == "Eeyore":
        print("Thanks for noticing me.")
    else if character == "Christopher Robin":
        print("Silly old bear.")
    else:
        print("Sorry! I don't know " + character "+'s catchphrase!")

# Tests
#welcome()
#greeting("Anthony")




# Problem Set 2:
def batman():
    print("I am vengeance. I am the night. I am Batman!")





# Advanced Problem Set 2:
# Q1:
def words_with_char(words, x):
    res = []
	for i in range(len(words)):
        if x in words[i]:
            res.append(i)
    return res

# Q2 (FizzBuzz variant):
def hulk_smash(n):
    res = []
	for i in range(1, n + 1):
        add = ""
        if i % 3 == 0:
            add = add + "Hulk"
        if i % 5 == 0:
            add = add + "Smash"
        if add:
            res.append(add)
        else:
            res.append(str(i))
    return res

# Q3:
def shuffle(message, indices):
	char_list = list(message)
    for i in range(len(message)):
        char_list[indices[i]] = message[i]
    return ''.join(char_list)

# Q4:
def minimum_boxes(meals, capacity):
	pass


# Tests
#batman()