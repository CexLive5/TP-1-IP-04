# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
i = 0
j = 0

def init(vals):
    global items, n, i, j
    items = list(vals)
    n = len(items)
    i = 0
    j = 0

def step():
    global items, n, i, j
    if i < n - 1:
        if j < n - i - 1:
            a = items[j]
            b = items[j + 1]
            if a > b:
                items[j], items[j + 1] = items[j + 1], items[j]
                swap = True
            else:
                swap = False
            j += 1
            return {"a": j - 1, "b": j, "swap": swap, "done": False}
        else:
            j = 0
            i += 1
            return step()
    return {"done": True}
 