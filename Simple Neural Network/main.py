import writerjson
class NeuralNetwork():

    def __init__(self, weights_file, result_file, input_file):
        #format replaces {} with item, :12 ensures 12 spaces reserved per word
        print("\n\n{:12}{:12}{:12}{}\n\n".format("Starting", "Awesome", "Neural", "Network"))
        
        try:
            #assiges each variable the given json folder
            self.layered_weights, self.result_interpreter, self.input_requests = map(writerjson.Read, (str(weights_file), str(result_file), str(input_file)))
        except:
            raise Exception("The code has an issue, please hold")
        
        #inputs = [1 if input(str(f'{question} y/n\n> ')) == 'y' else 0 for question in self.input_requests] # get the input for neural network
        inputs = self.input_requests #for non user input
        # list[item] is 1 if 'y'                                    else 0 for every question prompted
        refeed = [self.fire_neuron(inputs) for self.current_layer in self.layered_weights if self.current_layer != 'final'][-1]
        #         repetative loop          for every layer                      if current layer is not final but only save last loop
        
        # could simply put refeed term into next bracket below, but makes code harder to comprehend
        self.output = self.final_result(refeed) # runs for the final last loop # interpretes and returns the result

    def fire_neuron(self, refeed): # actuall calculation
        # just how far can you compress something in python???? (used to be 8 lines, now just 1)
        return [
            # 1 if sum of weight * neuron of previous layer for every weight of neuron >= activation threshold, else 0
            1 if sum(int(weight) * int(refeed[index]) for index, weight in enumerate(neuron[:-1])) >= neuron[-1] else 0 
            # runs for every neuron in the layer
            for neuron in self.layered_weights[str(self.current_layer)]
            ]

    def final_result(self, refeed):
        self.result = str(sum(refeed[index] * self.layered_weights['final'][index] for index in range(len(refeed))))
        try:
            return self.result_interpreter[self.result]
        except:
            return "failed", self.result
    
    def __str__(self): # required to get a string as output instead of pointer
        return f"\n{self.output}"




if __name__ == '__main__': # only runs if this file is selected

    while True:
        inputs = "inputs_cross" if input(str("Cross y/n\n> ")) == 'y' else "inputs_circle"
        print(NeuralNetwork("weights_pic", "results_pic", inputs)) # print and run results