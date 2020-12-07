import re


#Datastrucutre. Dictionary with keys being the name of the bag, the value is the bag object
# The bag object contains a string signinifying which bag this is
# as well as a dictionary specifying what this bag can contain. Keys are the names of the bags, value is how many of them.
# I will probably want a dictionary for memoizing if a bag can contain a gold bag or not, but that's dependant on the final runtime.


# Can any bags contain themselves? Can any bags contain bags which can contain themselves? (I.E. are there loops?)

class Bag:
    def __init__(self, name, listOfContents):
        self.name = name
        self.listOfContents = listOfContents

def bagsWithinBag(bagName, dictOfBags, memoMap):

    bag = dictOfBags[bagName]
    contains = bag.listOfContents
    if bagName in memoMap:
        return memoMap[bagName]
    if not contains:
        memoMap[bagName] = 0
        return 0
    else:
        count = 0
        for otherBag, k in contains.items():
            count += int(k) *  (1 +  bagsWithinBag(otherBag, dictOfBags, memoMap))
        memoMap[bagName] = count
        return count

def canContainGolden(bagName, dictOfBags, memoMap):

    bag = dictOfBags[bagName]
    contains = bag.listOfContents
    if bagName in memoMap:
        return memoMap[bagName]
    if not contains:
        memoMap[bagName] = False
        return False
    elif "shiny gold" in contains:
        memoMap[bagName] = True
        return True
    else:
        for otherBag in contains:
            if canContainGolden(otherBag, dictOfBags, memoMap):
                memoMap[bagName] = True
                return True
        memoMap[bagName] = False
        return False

bags = dict()
lineMatchRe = re.compile(r"^([a-z]+ [a-z]+) bags contain (?:(\d+) ([a-z]+ [a-z]+)|no other) bags?(?:, (\d+) ([a-z]+ [a-z]+) bags?)*.$")
bagMatchRe = re.compile(r"^([a-z]+ [a-z]+)")
containsMatchRe = re.compile(r"(?:(\d+) ([a-z]+ [a-z]+)|no other) bags?")

with open("input.txt") as file_in:
    for line in file_in:
        line = line.rstrip()
        m = bagMatchRe.match(line)
        name = m.group(1)
        newStr = line[m.end(1):]
        c = containsMatchRe.search(newStr)
        if c.group(1) == None:
            dictOfBags = None
        else:
            dictOfBags = dict()
            while c:
                bagCount = c.group(1)
                bagName = c.group(2)
                dictOfBags[bagName] = bagCount
                newStr = newStr[c.end(2):]
                c = containsMatchRe.search(newStr)

        bag = Bag(name, dictOfBags)
        bags[name] = bag

memoMap = dict()

print(bagsWithinBag("shiny gold", bags, memoMap))


