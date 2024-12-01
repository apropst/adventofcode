with open('Data7-1.txt', 'r') as myfile:
	filedata = myfile.read().splitlines()

bagarr = []
solution = 0

class Bag:
    def __init__(self, name, contents):
        self.name = name
        self.contents = contents

class Rule:
    def __init__(self, quantity, bagtype):
        self.quantity = quantity
        self.bagtype = bagtype

def getParentBags(target):
    result = []
    for bag in bagarr:
        for rule in bag.contents:
            if (rule.bagtype == target):
                result.append(bag.name)
    return result

for line in filedata:
    rulearr = []
    base = ' '.join(line.split()[:2])
    rules = ' '.join(line.split()[4:]).split(", ")
    for rule in rules:
        if (rule == "no other bags."):
            rulearr.append(Rule("0", "None"))
        else:
            rulearr.append(Rule(rule[0], ' '.join(rule.split()[1:3])))
    bagarr.append(Bag(base, rulearr))

#for bag in bagarr:
#    print(bag.name + ":")
#    for rule in bag.contents:
#        print(rule.quantity + " " + rule.bagtype)
#    print()

print(getParentBags("shiny gold"))
#print(getParentBags("shiny gold"))