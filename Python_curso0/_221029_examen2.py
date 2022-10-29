def mystery(elements, max):
    accum =[]
    for elt in elements:
        if elt > max:
            accum.append(elt)
    return accum

mystery([],5)

def candida(elements, combiner, initial):
    accum = initial
    for elt in elements:
        accum = combiner(accum, elt)
    return accum

candida([1,2,34,56], lambda a,b:a+b, 0)

def g(elements, transformer):
    accum = []
    for elt in elements:
        accum.append(transformer(elt))
    return accum

def lens(matrix):
    return g(matrix, len)

lens([[1,2,3],[3,4],[5,6,7,8,9]])