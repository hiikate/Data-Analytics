class Mammals:
    pass
    def print_method(self): print(" Mammals don't lay eggs ")

class Dogs(Mammals):
    pass
    def print_method(self): print("Dogs bark")

class Cats(Mammals):
    pass
    def print_method(self): print("Cats hiss")


def main():
    print("In main method")
    y = Mammals()
    x = Dogs()
    z = Cats()
    y.print_method()
    x.print_method()
    z.print_method()

if __name__ == "__main__":
    main()