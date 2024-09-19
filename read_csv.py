import csv

#-------------------------- FUNCION DE LECTURA DEL ARCHIVO---------------------------------

def read_csv(path):
    with open(path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        data = []
        for row in reader:
            data.append(row)
        return data

def print_data(data):
    for item in data:
        print(item)
        print()


if __name__ == '__main__':
	data = read_csv('example.csv')
	print_data(data)