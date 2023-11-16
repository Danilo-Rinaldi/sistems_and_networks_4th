#CLASSI
class Quadrato():
    def __init__(self, lato):
        self.lato = lato
    def CalcolaArea(self):
        return self.lato**2
    def StampaLato (self):
        print(f"i lato è pari a {self.lato}")

    

def main ():
    q = Quadrato(4)
    print (f"l'area del quadrato è {q.CalcolaArea()}")
    q.lato = 5 #nulla èprivato su python
    q.StampaLato()


if __name__ == "__main__":
    main()