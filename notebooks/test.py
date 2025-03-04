import pickle
x = {"a": 1, "b": {"c": 2, }, }
pickle.dump(x, open("thing.bin", "wb+"))