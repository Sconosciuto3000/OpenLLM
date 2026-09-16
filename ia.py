import json
import os

# Assegnazione variabili
data1 = ""
data2 = {}

mem = {}
mem1 = {}
mem2 = {}

# Funzioni
def gen2(words, debug=False):
    global data2
    response = []
    if debug:
        print(words, type(words))
    if data2 == {}:
        path = os.path.join("model", "data2.json")
        with open(path, "r") as f:
            data2 = json.load(f)
    founded_index = []
    if debug:
        print(data2, type(data2))
    for indx in range(len(words)):
        if debug:
            print(indx)
        for ind, cont in dict(data2["index"]).items():
            if debug:
                print(words[indx], list(cont))
            try:
                if words[indx] in list(cont) and words[indx+1] in list(cont):
                    if ind not in founded_index:
                        founded_index.append(ind)
                        if debug:
                            print(words[indx], list(cont))
                            print("ok")
                            print(data2[ind])
                        response.append(data2[ind])
            except:
                pass
    return response

def gen1(keys, words, debug=False):
    global data1
    if keys == []:
        return "Database scarso"
    response = ""
    riflessivi = {"mi": ["tu", "ti"], "ti": ["io", "mi"], "si": ["lui", "si"], "ci": ["noi", "ci"], "vi": ["voi", "vi"]}
    persone = {"io": ["user", "sing", "nd", "ti"], "tu": ["ai", "sing", "f", "mi"], "lui": ["other", "sing", "m", "si"], "lei": ["other", "sing", "f", "si"], "noi": ["other", "plur", "multi", "ci"], "voi": ["other", "plur", "multi", "vi"], "loro": ["other", "plur", "multi", "si"]}
    verbi = {"mi": "i", "ti": "o", "si": {"lui": "a", "loro": "ano"}, "ci": "amo", "vi": "ate"}

    riflessivi_frase = list(set(riflessivi) & set(words))
    if riflessivi_frase != []:
        temp_words = words
        for x in riflessivi_frase:
            temp_words.remove(x)
        for index in range(0, len(temp_words) - 1):
            if debug:
                print(index)
            if temp_words[index][-1] not in verbi.values():
                temp_words.pop(index)
        if len(temp_words) == 1:
            verbo_n_fine = 0 - len(str(verbi[riflessivi_frase[0]]))
            verbo = str(temp_words[0])
            if "si" not in riflessivi_frase:
                verbo_fine = verbi[riflessivi_frase[0]]
                verbo_p1 = verbo[0:verbo_n_fine]
                verbo = verbo_p1 + verbo_fine
            for x in riflessivi[riflessivi_frase[0]]:
                response += x + " "
            response += str(verbo + " " + keys[0])
    else:
        if debug:
            print(keys)
        for resp in keys:
            response += resp
            
    return response
    
# Logica

while True:
    inp = input("Inserisci la domanda: ")

    inp = inp.replace(".", "")
    inp = inp.replace(",", "")
    inp = inp.replace(";", "")
    inp = inp.replace(":", "")
    inp = inp.replace("?", "")
    inp = inp.replace("!", "")
    inp = inp.lower()

    found = False
    for exa, res in mem.items():
        if inp in exa:
            output = gen1(res)
            found = True

    if not found:
        gen2output = gen2(inp.split(), debug=False)
        output = gen1(gen2output, inp.split(), debug=False)

    print(output)
