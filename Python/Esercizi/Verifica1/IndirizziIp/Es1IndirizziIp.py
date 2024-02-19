#Dato in input un indirizzo ipv4 e la sua relativa subnet mask 
#controllare se è un indirizzo privato oppure di loopback
#se indirizzo rete? se è valido? stampare tutti gli indirizzi ip disponibili

import ipaddress

def main():

    ip = input("dammi un ip: ")

    sm = input("dammi una Subnet mask (es. /24):")

    Ipv4Pieno = ip + sm

    ip = ipaddress.IPv4Address(ip)

    if ip.is_private:
        print("è un ip privato")
    else:
        print("è un ip pubblico")

    iprete = ipaddress.ip_network(Ipv4Pieno, strict=False)
    #se gli do un true allora lui vuole perforza un ip di rete ma con false io posso dargli qualsiasi ip e 
    # lui si calcola l'ip di ret automaticamente

    if ip.is_loopback:
        print("l'ip è di loopback")
    else:
        print("l'ip di non è di loopback")

    if Ipv4Pieno == str(iprete):
        print ("è di rete perché")
    else:
        print("non è di rete perché")

    print(f"indirizzo di rete: {iprete}")

    host = list (iprete.hosts())
    print(f"il primo ip utilizzabile è {host[0]} e l'ultimo è {host[-1]}")




    






if __name__ == "__main__":
    main()