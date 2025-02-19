import random
class PolynomialTerm:
    def __init__(self):
        self.n = None
        self.p = None
    def __str__(self):
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
    def _clean(self):
        for i in range(len(self.terms)):
            for j in range(i+1, len(self.terms) - 1):
                if self.terms[i].p == self.terms[j].p:
                    self.terms[i].n += self.terms[j].n
                    del self.terms[j]
        self.terms.sort(key=lambda x: x.p)
    def fromexpr(self, strexpr: str):
        #print(f"building with {strexpr}")
        self.terms = []
        for strterm in strexpr.split("+"):
            t = PolynomialTerm()
            t.fromexpr(strterm)
            self.terms.append(t)
        self._clean()
    def __str__(self):
        return "+".join(list(map(lambda term: str(term), self.terms)))
    def mul(self, other_poly):
        poly = Polynomial()
        ts = []
        for t1 in self.terms:
            for t2 in other_poly.terms:
                nt = PolynomialTerm()
                nt.n = t1.n * t2.n
                nt.p = t1.p + t2.p
                ts.append(nt)
        poly.terms = ts
        poly._clean()
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
        print(f"({p1}) * ({p2}) = {p1.mul(p2)}")
if __name__ == "__main__":
    test(3)
