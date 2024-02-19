class Testo():
    def __init__(self, frase, cifrata, chiave, dizLetNum, dizNumLet):
        self.frase = frase.lower()
        self.cifrata = cifrata.lower()
        self.chiave = chiave.lower()
        self.dizLetNum = dizLetNum
        self.dizNumLet = dizNumLet

    def decifra(self):
        
        
        cifrataNum = [self.dizLetNum[carattere] for carattere in self.cifrata]
        chiaveNum = [self.dizLetNum[carattere] for carattere in self.chiave]

        sottrazione = [(cifrata - chiave) % 21 for cifrata, chiave in zip(cifrataNum, chiaveNum)]

        decifrata = ''

        #decifrata = ''.join([self.dizNumLet[num] for num in sottrazione])
        for num in sottrazione:
            decifrata = decifrata + self.dizNumLet[num]

        return decifrata

        


    def cifra(self):
        parolaNum = [self.dizLetNum[carattere] for carattere in self.frase]
        chiaveNum = [self.dizLetNum[carattere] for carattere in self.chiave]

        somma = [(parolaNum[numero] + chiaveNum[numero]) % 21 for numero in range(len(parolaNum))]

        self.cifrata = ''.join([self.dizNumLet[num] for num in somma])

        return self.cifrata
    

class Testo2 ():
    pass

def main():

    dizLetNum = {
        'a': 0,
        'b': 1,
        'c': 2,
        'd': 3,
        'e': 4,
        'f': 5,
        'g': 6,
        'h': 7,
        'i': 8,
        'l': 9,
        'm': 10,
        'n': 11,
        'o': 12,
        'p': 13,
        'q': 14,
        'r': 15,
        's': 16,
        't': 17,
        'u': 18,
        'v': 19,
        'z': 20,
        ' ': 21
    }

    dizNumLet = {}

    for chiave in dizLetNum:
        dizNumLet[dizLetNum[chiave]] = chiave

    """
    dizNumLet = {
        0: 'a',
        1: 'b',
        2: 'c',
        3: 'd',
        4: 'e',
        5: 'f',
        6: 'g',
        7: 'h',
        8: 'i',
        9: 'l',
        10: 'm',
        11: 'n',
        12: 'o',
        13: 'p',
        14: 'q',
        15: 'r',
        16: 's',
        17: 't',
        18: 'u',
        19: 'v',
        20: 'z',
        21: ' '
    }
    
    """
    

    frase = input("Dimmi una frase: ")
    chiave = input("Dammi una chiave: ")

    cifrata = ''

    str_obj = Testo(frase, cifrata, chiave, dizLetNum, dizNumLet)

    print(str_obj.cifra())

    print(str_obj.decifra())

if __name__ == "__main__":
    main()
