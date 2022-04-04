from csv import reader
from random import randrange

class Perceptron:

    def __init__(self, file_name, accuracy):
        self.file_name = file_name
        self.accuracy = accuracy

    def predict(self, line, weights):
        activasion = weights[0]
        for i in range(len(line)-1):
            activasion += weights[i+1]*line[i]
        return 1.0 if activasion >= 0.0 else 0.0

    def calculate_accuracy(self, actual, predicted):
        correct = 0
        for i in range(len(actual)):
            if actual[i] == predicted[i]:
                correct += 1
        return correct/float(len(actual))*100.0
    
    def get_data_from_file(self):
        data = list()
        with open(self.file_name, 'r') as file:
            csv_reader = reader(file)
            for row in csv_reader:
                if row:
                    data.append(row)
        return data
    
    def store(self, vector):
        with open('help_file.csv', 'w') as file:
            file.write(f'{vector}\n')
            with open('training-data.csv', 'r') as help:
                csv_reader = help.readlines()
                for row in csv_reader:
                    if row:
                        file.write(row)
    
    def is_hit(self, scores):
        print('Correct guess' if sum(scores)/float(len(scores)) > 69.5 else 'Incorrect guess')

    def column_to_float(self, data, column):
        for row in data:
            row[column] = float(row[column].strip())

    def column_to_int(self, data, column):
        unique = set(row[column] for row in data)
        end = dict()

        for i, q in enumerate(unique):
            end[q] = i
        for row in data:
            row[column] = end[row[column]]
        return end

    def split_data(self, data, parts):
        split = list()
        l_data = list(data)
        for i in range(parts):
            tmp = list()
            while len(tmp) < parts:
                place = randrange(len(l_data))
                tmp.append(l_data.pop(place))
            split.append(tmp)
        return split

    def correct_algorithm(self, data, n_parts, *args):
        parts = self.split_data(data, n_parts)
        hits = list()
        for part in parts:
            work_set = list(parts)
            work_set.remove(part)
            work_set = sum(work_set, [])
            check_set = list()
            for row in part:
                copy = list(row)
                check_set.append(copy)
                copy[-1] = None
            shoot = self.logic(work_set, check_set, *args)
            real = [row[-1] for row in part]
            accuracy = self.calculate_accuracy(real, shoot)
            hits.append(accuracy)
        return hits

    def estimate_weights(self, data, l, n):
        weights = [0.0 for i in range(len(data[0]))]

        for ns in range(n):
            for row in data:
                prediction = self.predict(row, weights)
                error = row[-1] - prediction
                weights[0] += l*error
                for i in range(len(row)-1):
                    weights[i+1] += l*error*row[i]
        return weights

    def logic(self, data, test, l, n):
        predctions = list()
        for row in test:
            predction = self.predict(row, self.estimate_weights(data, l, n))
            predctions.append(predction)
        return(predctions)
