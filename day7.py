lines = [line.strip() for line in open("input.txt", 'r').readlines()]

variables = {}

for line in lines:
    left, right = line.split(" -> ")
    if "NOT" in left:
        op, var = left.split()
        if var not in variables:
            continue
        variables[right] = 65535 - variables[var]
    elif "RSHIFT" in left:
        var, op, val = left.split()
        if var not in variables:
            continue
        variables[right] = variables[var] >> int(val)
    elif "LSHIFT" in left:
        var, op, val = left.split()
        if var not in variables:
            continue
        variables[right] = variables[var] << int(val)
    elif "OR" in left:
        var1, op, var2 = left.split()
        if var1 not in variables or var2 not in variables:
            continue
        variables[right] = variables[var1] | variables[var2]
    elif "AND" in left:
        var1, op, var2 = left.split()
        if var1 not in variables or var2 not in variables:
            continue
        print(var1, var2)
        variables[right] = variables[var1] & variables[var2]
    else:
        if left in variables:
            variables[right] = variables[left]
        else:
            variables[right] = int(left)

print(variables["a"])
