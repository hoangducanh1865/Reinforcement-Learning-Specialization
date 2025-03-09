import pickle

# Data to be serialized
data = {'key': 'value', 'number': 42}

# Serialize the data and save it to a file
with open('data.pkl', 'wb') as file:
    pickle.dump(data, file)

# Deserialize the data from the file
with open('data.pkl', 'rb') as file:
    loaded_data = pickle.load(file)

print(loaded_data)  # Output: {'key': 'value', 'number': 42}