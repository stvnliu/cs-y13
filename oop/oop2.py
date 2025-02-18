class greeting:
    def hello(self, fname = None, lname = None):
        print(f"Hello {fname if fname else ''} {lname if lname else ''}!")
g = greeting()
g.hello()
g.hello("John")
g.hello("John", "Doe")
