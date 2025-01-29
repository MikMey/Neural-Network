import writerjson

layered_weights = writerjson.Read('weights') #{'layer 1':[[w1,w2, ..., wn, neuron activation threshold], [], ..., []], 'layer n': [[],...]}
result_interpreter = writerjson.Read('results') #{'0': 'Banana, '1': Orange, ...}

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
    res = []
    check_sum = 0
    for i, x in enumerate(current_layer): # for every neuron on layer
        for j, y in enumerate(prev_layer): # for every neuron on previous layer
            check_sum += int(current_layer[i][j]) * int(prev_layer[j]) # check sum += weight * active or deactive prev layer neuron
        if check_sum >= current_layer[i][-1]:
            res.append(1)
        else:
            res.append(0)
        check_sum = 0
    return res

def final_result(layer_res):
    check_sum = 0
    for index, i in enumerate(layer_res):
        check_sum += layer_res[index] * layered_weights['final'][index]
    return check_sum

def interpret_res(res):
    res = str(res)
    try:
        return result_interpreter[res]
    except:
        return "failed", res

def run_in_order():
    refeed = ask_input()
    for i, current_layer in enumerate(layered_weights):
        if i <= 1:
            continue
        refeed = fire_neuron(refeed, layered_weights[str(current_layer)])
    result = final_result(refeed)
    return interpret_res(result)

if __name__ == '__main__':
    while True:
        print(run_in_order())