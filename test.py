import pickle

test = "test ptn "
list = [0,0,0,0,0,0,0,0,0]
pickle.dump(test, open("variables.txt", "wb"))
variable = pickle.load(open("variables.txt", "rb"))

print(variable)

