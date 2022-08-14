import numpy as np
from comparisonParser import *
from parser import NumericStringParser


class Piecewise:
    def __init__(self, functions):
        self.functions = functions

    def __repr__(self):
        lines = []
        for i in range(len(self.functions)):
            if i == int(len(self.functions)/2):
                lines.append(f"f(x) = {self.functions[i]}")
            else:
                lines.append(f"ㅤㅤㅤㅤ{self.functions[i]}")
        return "\n".join(lines)

    def __iter__(self):
        for func in self.functions:
            yield func

    def getGraphPoints(self, graphRange, depth=0.1):
        parser = NumericStringParser()

        points = {}
        for func in self.functions:
            points[self.functions.index(func)] = (func.eq, [])

        digits = len("".join(str(depth).split(".")))
        for i in np.arange(graphRange[0], graphRange[1], depth):
            x = round(float(i), digits)

            function = None
            for func in self:
                if evaluate(func.rule, x):
                    function = func

            toEval = function.eq.replace("x", str(x))
            try:
                points[self.functions.index(function)][1].append((i, parser.eval(toEval)))
            except ZeroDivisionError:
                pass

        return points