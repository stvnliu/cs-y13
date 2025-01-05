import random
class PolynomialTerm:
    def __init__(self):
        self.n = None
        self.p = None
    def strexpr(self):
        return f"{self.n if self.n != 1 else ''}x^{self.p}"
    def fromexpr(self, txt: str):
        if txt[0] == 'x':
            txt = '1'+ txt
        #print(f"received {txt}")
        l = txt.split("x^")
        if len(l) != 2:
            raise ValueError(l)
        n_str: str = l[0]
        p_str: str = l[1]
        if (not n_str.isnumeric()) or (not p_str.isnumeric()):
            raise ValueError(n_str)
        self.n = int(n_str)
        self.p = int(p_str)
        return
class Polynomial:
    def __init__(self):
        return
    def fromexpr(self, strexpr: str):
        #print(f"building with {strexpr}")
        self.terms = []
        for strterm in strexpr.split("+"):
            #print(f"parsing {strterm}")
            t = PolynomialTerm()
            t.fromexpr(strterm)
            #print(t.strexpr())
            self.terms.append(t)
        self.terms.sort(key=lambda x: x.p)
    def strexpr(self):
        return "+".join(list(map(lambda term: term.strexpr(), self.terms)))
    def mul(self, other_poly):
        poly = Polynomial()
        ts = []
        for t1 in self.terms:
            for t2 in other_poly.terms:
                nt = PolynomialTerm()
                nt.n = t1.n * t2.n
                nt.p = t1.p + t2.p
                add = True
                for t in ts:
                    if nt.p == t.p:
                        t.n += nt.n
                        add = False
                if not add: continue
                ts.append(nt)
        poly.terms = ts
        return poly
def test(limit: int):
    for i in range(10):
        p1 = Polynomial()
        p2 = Polynomial()
        str1 = ""
        str2 = ""
        n1 = random.randint(1, limit)
        n2 = random.randint(1, limit)
        for i in range(n1):
            str1 += f"{random.randint(1, 10)}x^{random.randint(1, 10)}" + ("+" if i != n1-1 else "")
            #print(str1)
        for i in range(n2):
            str2 += f"{random.randint(1, 10)}x^{random.randint(1, 10)}" + ("+" if i != n2-1 else "")
        p1.fromexpr(str1)
        p2.fromexpr(str2)
        print(f"({p1.strexpr()}) * ({p2.strexpr()}) = {p1.mul(p2).strexpr()}")
if __name__ == "__main__":
    test(3)
