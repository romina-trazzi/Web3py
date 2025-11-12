import pickle

data = pickle.load( open("transactions.pkl", "rb" ))
# print(data)

print('Retrieved pickled data:')
for i, item in enumerate(data):
    print(f'Data {i}: {item}')