import os
from random import seed
from Perceptron import Perceptron

file = input('Enter name of a file: ')
precision = float(input('Enter value of precision: '))

perceptron = Perceptron(file, precision)
seed(1)

data = perceptron.get_data_from_file()

for i in range(len(data[0])-1):
    perceptron.column_to_float(data, i)

perceptron.column_to_int(data, len(data[0])-1)
scores = perceptron.correct_algorithm(data, 5 if file.find("test-data.csv") != -1 else 2, precision, 600)

print(f'\nAccuracy: {(sum(scores)/float(len(scores)))}%\n')

vector = input('Podaj przykladowy vektor do sprawdzenia, jesli chcesz zakonczyc wpisz end\n')

while vector != 'end':
    perceptron.file_name = 'help_file.csv'
    perceptron.store(vector)

    data = perceptron.get_data_from_file()
    os.remove(perceptron.file_name)
    for i in range(len(data[0])-1):
        perceptron.column_to_float(data, i)

    perceptron.column_to_int(data, len(data[0])-1)
    scores = perceptron.correct_algorithm(data, 5, precision, 100)

    print('Correct guess' if sum(scores)/float(len(scores)) > 69.5 else 'Incorrect guess')
    vector = input('Podaj przykladowy vektor do sprawdzenia, jesli chcesz zakonczyc wpisz end\n')