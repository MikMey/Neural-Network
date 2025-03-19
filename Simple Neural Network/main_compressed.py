import writerjson
class NeuralNetwork():
    def __init__(self, weights_file, result_file, input_file):
        print("\n\n{:12}{:12}{:12}{}\n\n".format("Starting", "Awesome", "Neural", "Network"))
        self.layered_weights, self.result_interpreter, self.input_requests = map(writerjson.Read, (str(weights_file), str(result_file), str(input_file)))
        inputs = [1 if input(str(f'{question} y/n\n> ')) == 'y' else 0 for question in self.input_requests] 
        self.output = self.final_result([[1 if sum(int(weight) * int(inputs[index]) for index, weight in enumerate(neuron[:-1])) >= neuron[-1] else 0 for neuron in self.layered_weights[str(self.current_layer)]] for self.current_layer in self.layered_weights if self.current_layer != 'final'][-1])
    def final_result(self, refeed):
        self.result = str(sum(refeed[index] * self.layered_weights['final'][index] for index in range(len(refeed))))
        return self.result_interpreter[self.result]
    def __str__(self):
        return f"\n{self.output}"
    
#holy shit what is this

if __name__ == '__main__': # only runs if this file is selected

    while True:
        print(NeuralNetwork("weights", "results", "inputs")) # print and run results