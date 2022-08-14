def evaluate(rule, x):
    rule = rule.replace("x", str(x))
    if not __verify(rule):
        raise ValueError("Rule did not pass verification")
    return eval(rule)


def __verify(rule):
    parts = rule.split()
    ops = ["<", "<=", ">=", ">", "-"]
    for part in parts:
        if part not in ops:
            try:
                float(part)
            except:
                return False
    return True
