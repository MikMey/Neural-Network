import writerjson
class NeuralNetwork():

    def __init__(self, weights_file, result_file, input_file):
        print("\n\nStarting\n\n")
        
        try:
            self.layered_weights = writerjson.Read(str(weights_file)) #{'layer 1':[[w1,w2, ..., wn, neuron activation threshold], [], ..., []], 'layer n': [[],...]}
            self.result_interpreter = writerjson.Read(str(result_file)) #{'0': 'Banana, '1': Orange, ...}
            self.input_requests = writerjson.Read(str(input_file))
        except:
            raise Exception("The code has an issue, please hold")
        refeed = self.ask_input() # get the input for neural network
        refeed = [self.fire_neuron(refeed) for self.current_layer in self.layered_weights if self.current_layer != 'final'][-1]
        #         repetative loop          for every layer                      if current layer is not final but only save last loop
        # could simply put refeed term into next bracket below, but makes code harder to comprehend
        self.output = self.final_result(refeed) # runs for the final last loop # interpretes and returns the result
        
        #self.run_in_order()

    def ask_input(self):
        inputs = [
            1 if input(str(f'{question} y/n\n> ')) == 'y'
            else 0
            for question in self.input_requests
        ]
        
        return inputs # inputs = [i1,i2,i3]

    def fire_neuron(self, refeed): # actuall calculation
        res = []
        for i, current_item in enumerate(self.layered_weights[str(self.current_layer)]): # for every neuron on layer
            check_sum = 0
            for j, refeed_item in enumerate(refeed): # for every neuron on previous layer
                check_sum += int(current_item[j]) * int(refeed_item) # check sum += weight * active or deactive prev layer neuron
            if check_sum >= current_item[-1]:
                res.append(1)
            else:
                res.append(0)
        return res

    def final_result(self, refeed):
        self.result = str(sum(refeed[index] * self.layered_weights['final'][index] for index in range(len(refeed))))
        try:
            return self.result_interpreter[self.result]
        except:
            return "failed", self.result

    # def run_in_order(self):
    #     refeed = self.ask_input() # get the input for neural network
    #     refeed = [self.fire_neuron(refeed) for self.current_layer in self.layered_weights if self.current_layer != 'final'][-1]
    #     #         repetative loop          for every layer                      if current layer is not final but only save last loop
    #     # could simply put refeed term into next bracket below, but makes code harder to comprehend
    #     self.output = self.final_result(refeed) # runs for the final last loop # interpretes and returns the result
    
    def __str__(self): # required to get a string as output instead of pointer
        return f"\n{self.output}"




if __name__ == '__main__': # only runs if this file is selected

    while True:
        print(NeuralNetwork("weights", "results", "inputs")) # print and run results