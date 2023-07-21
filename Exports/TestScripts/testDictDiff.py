#def diff_class(classDict):

#NOTE There's probably a module to do this already, look for it

testA = {"a":1,"b":{"b2":{"b22":150},"b3":100},"c":"end"}
testB = {"a":1,"b":{"b2":99,"b3":100},"c":"end"}

def checkDict(dictC,identifier):
    print("-----------------------------")
    for _key in dictC:
        if type(dictC[_key]) == dict:
                #print(f"Item Dict:({_key}) {dictC[_key]}")
                dictRecurse(dictC[_key],_key,identifier)
        else:
                print(f"[{identifier}] Item other: ({_key}) {dictC[_key]}")
    print("-----------------------------")

def dictRecurse(_dict,key,identifier):
    if type(_dict) == dict:
        for _key in _dict:
            if type(_dict[_key]) == dict:
                dictRecurse(_dict[_key],_key,identifier)
            else:
                print(f"[{identifier}] Item in dict: ^({key}) ({_key}) {_dict[_key]}")

checkDict(testA,"1")
checkDict(testB,"2")