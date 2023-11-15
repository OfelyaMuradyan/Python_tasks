import json

def store_data(file_name):
    try:
        with open(file_name, 'r') as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []
    return data

def save_data(file_name, data):
    try:
        with open(file_name, 'w') as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"An error occurred: {e}")

def add_data(data, new_data):
    data.append(new_data)

def retrieve_data(data):
    if data:
        for i in data:
            print(i)
    else:
        print("There is no data")

def update_data(data, target, new_data):
    for item in data:
        if target in item:
            item.update(new_data)

def delete_data(data, target):
    old_data = len(data)
    data = [item for item in data if target not in item]
    if len(data) == old_data:
        print("Data not found.")

file_name = input('Enter File name: ')
data = store_data(file_name)

def data_management(func):
    if func == 'add':
        new_data = input("Enter data to add: ")
        add_data(data, new_data)
        save_data(file_name, data)
    elif func == 'retrieve':
        retrieve_data(data)
    elif func == 'update':
        target = input("Enter the data to update: ")
        new_data = input("Enter the new data: ")
        update_data(data, target, new_data)
        save_data(file_name, data)
    elif func == 'delete':
        target = input("Enter the data to delete: ")
        delete_data(data, target)
        save_data(file_name, data)
    else:
        print("Invalid input")

data_management('add')
print("Data changed")