import pickle

pickle_in = open("lstm_e1_b1.pickle","rb")
model = pickle.load(pickle_in)

print(model)