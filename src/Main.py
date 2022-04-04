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

scores = perceptron.correct_algorithm(data, 2, precision, 900)

print(f'Scores: {scores}')
print(f'Accuracy: {(sum(scores)/float(len(scores)))}')