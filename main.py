class neuralnetwork():
    import writerjson

    def __init__(self, weights_file, result_file):
        self.layered_weights = writerjson.Read(str(weights_file)) #{'layer 1':[[w1,w2, ..., wn, neuron activation threshold], [], ..., []], 'layer n': [[],...]}
        self.result_interpreter = writerjson.Read(str(result_file)) #{'0': 'Banana, '1': Orange, ...}
        self.run_in_order()

    def ask_input(self):
        inputs = []
        inputs.append(input(str('Does your item weigh more than 100g? y/n\n> ')))
        inputs.append(input(str('Is your item red? y/n\n> ')))
        inputs.append(input(str('Is your item round? y/n\n> ')))
        
        for index, i in enumerate(inputs):
            if i == 'y':
                inputs[index] = 1
            else:
                inputs[index] = 0
        return inputs # inputs = [i1,i2,i3]

    def fire_neuron(self, refeed, current_layer):
        res = []
        check_sum = 0
        for i, x in enumerate(current_layer): # for every neuron on layer
            for j, y in enumerate(refeed): # for every neuron on previous layer
                check_sum += int(current_layer[i][j]) * int(refeed[j]) # check sum += weight * active or deactive prev layer neuron
            if check_sum >= current_layer[j][-1]:
                res.append(1)
            else:
                res.append(0)
            check_sum = 0
        return res

    def final_result(self, refeed):
        check_sum = 0
        for index, i in enumerate(refeed):
            check_sum += refeed[index] * self.layered_weights['final'][index]
        return check_sum

    def interpret_res(self):
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
        self.result = self.final_result(refeed) # runs for the final last loop
        self.output = self.interpret_res() # interpretes and returns the result
    
    def __str__(self):
        return f"\n{self.output}"




if __name__ == '__main__': # only runs if this file is selected
    import writerjson
    
    while True:
        print("\n\nStarting\n\n")
        print(neuralnetwork("weights", "results")) # print and run results