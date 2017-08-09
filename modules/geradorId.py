def geraId(nome):
        newKey = 0
        weight = 1
        for s in nome:
            newKey += ord(s) * weight
            weight += 1
        return newKey