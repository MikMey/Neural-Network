import writerjson

def ask_input():
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

def fire_neuron(prev_layer, current_layer):
    print(current_layer)
    res = []
    check_sum = 0
    for i, x in enumerate(current_layer): # for every neuron on layer
        for j, y in enumerate(prev_layer): # for every neuron on previous layer
            check_sum += int(current_layer[i][j]) * int(prev_layer[j]) # check sum += weight * active or deactive prev layer neuron
        if check_sum >= current_layer[j][-1]:
            res.append(1)
        else:
            res.append(0)
        check_sum = 0
    return res

def final_result(layer_res, layered_weights):
    check_sum = 0
    for index, i in enumerate(layer_res):
        check_sum += layer_res[index] * layered_weights['final'][index]
    return check_sum

def interpret_res(res, result_interpreter):
    res = str(res)
    try:
        return result_interpreter[res]
    except:
        return "failed", res

def run_in_order(layered_weights, result_interpreter):
    refeed = ask_input() # get the input for neural network
    for i, current_layer in enumerate(layered_weights): # run once for every layer
        if current_layer == 'final': 
            continue # skip last loop
        refeed = fire_neuron(refeed, layered_weights[str(current_layer)]) # repetative loop, runs calculations with weights
    result = final_result(refeed, layered_weights) # runs for the final last loop
    return interpret_res(result, result_interpreter) # interpretes and returns the result

if __name__ == '__main__': # only runs if this file is selected
    layer = writerjson.Read('weights') #{'layer 1':[[w1,w2, ..., wn, neuron activation threshold], [], ..., []], 'layer n': [[],...]}
    result = writerjson.Read('results') #{'0': 'Banana, '1': Orange, ...}
    while True:
        print("\n\nStarting\n\n")
        print(run_in_order(layer, result)) # print and run results