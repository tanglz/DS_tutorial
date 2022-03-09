
class Line:

    def __init__(self, s, e):
        self.s = s
        self.e = e
        self.dir = s.to_point(e)

    def to_string(self):
        return self.s + "->" + self.e

    @staticmethod
    def inbetween(a, b, c):
        return (a <= b and b <= c) or (c <= b and b <= a)

    def contains(self, x, y):
        cross = (self.s.x - x) * (self.e.y - y) - (self.e.x - x) * (self.s.y - y)
        return abs(cross) < 1e-9 and self.inbetween(self.s.x, x, self.e.x) and self.inbetween(self.s.y, y, self.e.y)

    def eval(self, lam):
        return [self.s.x + lam * self.dir.x, self.s.y + lam * self.dir.y]

    def seg_length(self):
        return self.dir.mag()

    @staticmethod
    def det(a, b, c, d):
        return a * d - b * c

    def intersect(self, l):
        den = self.det(self.dir.x, -l.dir.x, self.dir.y, -l.dir.y)
        if den == 0:
            return None
        numBeta = self.det(self.dir.x, l.s.x - self.s.x, self.dir.y, l.s.y - self.s.y)
        numLambda = self.det(l.s.x - self.s.x, -l.dir.x, l.s.y - self.s.y, -l.dir.y)
        if den < 0:
            den = -den
            numBeta = - numBeta
            numLambda = -numLambda
        if numBeta < 0 or numBeta > den:
            return None
        return 1.0 * numLambda / den
