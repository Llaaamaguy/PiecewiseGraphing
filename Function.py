class Function:
    def __init__(self, eq, rule):
        self.eq = eq
        self.rule = rule

    def __repr__(self):
        return f"{self.eq} if {self.rule}"
