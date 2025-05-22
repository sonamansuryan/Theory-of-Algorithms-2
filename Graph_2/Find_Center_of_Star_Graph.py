def findCenter(edges):
    a, b = edges[0]
    c, d = edges[1]
    if a == c or a == d:
        return a
    return b

raw_input = input("Ներմուծիր եզրերը (օրինակ՝ [1,2],[2,3],[4,2]): ")

raw_input = "[" + raw_input + "]"
edges = eval(raw_input)

center = findCenter(edges)
print("Գրաֆի կենտրոնն է՝", center)
