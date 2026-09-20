import glob
import os
import re

import thingy as stack
#imports and stuff

class jump:
    def unconditional(name):
        return name
# no check
    def greater(name):
        return name if stack.Stack[-1] > 0 else None

    def lower(name):
        return name if stack.Stack[-1] < 0 else None

    def equal(name):
        return name if stack.Stack[-1] == 0 else None
# checks >0 <0 ==0 respectivily

refrence = {
    "push": (stack.push, "num"),
    "pop": (stack.pop, None),
    "dot": (stack.dot, None),
    "add": (stack.add, None),
    "sub": (stack.sub, None),
    "mul": (stack.mul, None),
    "div": (stack.div, None),
    "swap": (stack.swap, None),
    "save": (stack.save, None),
    "load": (stack.load, None),
    "jmp": (jump.unconditional, "label"),
    "jmpg": (jump.greater, "label"),
    "jmpl": (jump.lower, "label"),
    "jmpe": (jump.equal, "label"),
}
# lookuptable

def tokenize(code):
    return re.findall(r"#|\S+", code)
# its named for a reason

def setup(tokens):
    labels = {}
    code = []
    i = 0
    while i < len(tokens):
        if tokens[i] == "#":
            #check if the token is a pound
            if i + 1 >= len(tokens):
                raise ValueError("label missing after #")
            labels[tokens[i + 1]] = len(code)
            i += 2
            # if it is get the lable assosiated with it
        else:
            code.append(tokens[i])
            i += 1
            # if its not then put it in a pile
    return code, labels
# this function as a whole acts as a whole
# i love totolagy lol
# the function is a filter; it makes 2 piles code and the tags (the #tag things check the docs)

def understand(tokens, labels):
    pos = 0
    steps = 0
    while pos < len(tokens):
        steps += 1
        if steps > 100000:
            raise RuntimeError("too many steps, check your loop")
        #please dont crash please dont crash
        token = tokens[pos]
        func, argkind = refrence[token]
        
        if argkind == "num":
            if pos + 1 >= len(tokens):
                raise ValueError(f"{token} needs a number")
            func(int(tokens[pos + 1]))
            pos += 2
            # if the function takes a number...lookahead for da number
        elif argkind == "label":
            if pos + 1 >= len(tokens):
                raise ValueError(f"{token} needs a label")
            name = tokens[pos + 1]
            if name not in labels:
                raise ValueError(f"no such label: {name}")
            if func(name) is not None:
                pos = labels[name]
            else:
                pos += 2
            # if da function takes a lable look though the lable pile for it
        else:
            func()
            pos += 1
        # if it takes no arguments then... do the thing without args


here = os.path.dirname(os.path.abspath(__file__))
blobfish = sorted(glob.glob(os.path.join(here, "*.blobfish")))
#lookaround for the file
# #bestnameever

if blobfish:
    for blob in blobfish:
        code, labels = setup(tokenize(open(blob).read()))
        understand(code, labels)
    # read the blobfish
else:
    print("no blobfish in sight")
    
    # gofish