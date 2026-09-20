import glob
import os

import thingy as stack

keypass = ["push"]

refrence = {
    "push": stack.push,
    "pop": stack.pop,
    "dot": stack.dot,
    "add": stack.add,
    "sub": stack.sub,
    "mul": stack.mul,
    "div": stack.div,
    "swap": stack.swap,
    "save": stack.save,
    "load": stack.load,
}

def tokenize(code):
    tokens = code.split()
    return tokens

def understand(tokens):
    pos = 0
    while pos < len(tokens):
        token = tokens[pos]

        if token in refrence and token in keypass:
            if pos + 1 < len(tokens):
                refrence[token](int(tokens[pos + 1]))
                pos += 2
            else:
                raise ValueError(f"{token} is missing its argument")
        elif token in refrence:
            refrence[token]()
            pos += 1
        else:
            pos += 1

here = os.path.dirname(os.path.abspath(__file__))
blobfish = sorted(glob.glob(os.path.join(here, "*.blobfish")))

if blobfish:
    for blob in blobfish:
        with open(blob) as f:
            understand(tokenize(f.read()))
else:
    print("no blobfish in sight")