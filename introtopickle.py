import pickle

example_dict = {1:"6",2:"2",3:"f"}

pickle_out = open("dict.pickle","wb")
pickle.dump(example_dict, pickle_out)
pickle_out.close()
pickle_in = open("dict.pickle","rb")
test = pickle.load(pickle_in)
print(test)
print(test[3])