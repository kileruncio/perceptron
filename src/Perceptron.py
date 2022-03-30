from csv import reader

class Perceptron:

    def __init__(self, file_name, accuracy):
        self.file_name = file_name
        self.accuracy = accuracy
        print('You\'ve created a perceptron')
        # get_data_from_file(file_name)

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
    
