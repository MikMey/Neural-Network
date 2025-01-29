import json


def Recode(dict, change):
    index = int(0)
    
    keyword = (input("Enter decodation key:\n"))#current: "key"
    
    for i, j in dict.items():#i = jack, j={}
        for x, y in j.items():#x = alter, y=18
            for item in y:#item = 1
                try:
                    num = ord(keyword[index])#num=ascii[k]
                except:
                    index = 0
                    num = ord(keyword[index])#num=ascii[k]

                if change == "add":
                    entry = ''.join(chr(ord(letter)+num) for letter in y)
                else:
                    entry = ''.join(chr(ord(letter)-num) for letter in y)

                
                index += 1
            dict[i][x] = entry

    return dict

def Read(file):
    with open(file + '.json', 'r') as f:
        mydict = json.load(f)

    #Recode(mydict, "")
    print("Downloaded\n")
    return mydict

def Write(mydict, file):
    #Recode(mydict, "add")

    with open(file + '.json', 'w') as f:
        json.dump(mydict, f, indent=2)
        print("Saved!\n")