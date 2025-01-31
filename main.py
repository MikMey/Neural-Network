import writerjson
class neuralnetwork():

    def __init__(self, weights_file, result_file, input_file):
        print("\n\nStarting\n\n")
        
        try:
            self.layered_weights = writerjson.Read(str(weights_file)) #{'layer 1':[[w1,w2, ..., wn, neuron activation threshold], [], ..., []], 'layer n': [[],...]}
            self.result_interpreter = writerjson.Read(str(result_file)) #{'0': 'Banana, '1': Orange, ...}
            self.input_requests = writerjson.Read(str(input_file))
        except:
            raise Exception("The code has an issue, please hold")
        
        self.run_in_order()

    def ask_input(self):
        inputs = [] # initiate inputs
        for x, question in enumerate(self.input_requests): # for every question in file, ask question
            inputs.append(input(str(f'{question} y/n\n> ')))
        
        for index, i in enumerate(inputs): # convert y/n to 1/0
            if i == 'y':
                inputs[index] = 1
            else:
                inputs[index] = 0
        return inputs # inputs = [i1,i2,i3]

    def fire_neuron(self, refeed, current_layer): # actuall calculation
        res = []
        for i, x in enumerate(current_layer): # for every neuron on layer
            check_sum = 0
            for j, y in enumerate(refeed): # for every neuron on previous layer
                check_sum += int(current_layer[i][j]) * int(refeed[j]) # check sum += weight * active or deactive prev layer neuron
            if check_sum >= current_layer[j][-1]:
                res.append(1)
            else:
                res.append(0)
        return res

    def final_result(self, refeed):
        self.result = 0
        for index, i in enumerate(refeed):
            self.result += refeed[index] * self.layered_weights['final'][index]
        self.result = str(self.result)
        try:
            return self.result_interpreter[self.result]
        except:
            return "failed", self.result

    def run_in_order(self):
        refeed = self.ask_input() # get the input for neural network
        for i, current_layer in enumerate(self.layered_weights): # run once for every layer
            if current_layer == 'final': 
                continue # skip last loop
            refeed = self.fire_neuron(refeed, self.layered_weights[str(current_layer)]) # repetative loop, runs calculations with weights
        self.output = self.final_result(refeed) # runs for the final last loop # interpretes and returns the result
    
    def __str__(self): # required to get a string as output instead of pointer
        return f"\n{self.output}"




if __name__ == '__main__': # only runs if this file is selected

    while True:
        print(neuralnetwork("weights", "results", "inputs")) # print and run results