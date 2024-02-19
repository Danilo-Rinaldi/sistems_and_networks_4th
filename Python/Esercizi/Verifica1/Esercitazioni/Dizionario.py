dizionario = {"a": "albero", "b": "brutto", "c": "casa"}#indicizzato come voglio io
lista = ["albero", "brutto", "casa"]#indicizzato a numeri da 0 a -1

print(dizionario["b"])
print (lista[1])

dizionario["d"] = "dado"
lista.append("dado")

print (dizionario["d"])
print (lista[-1])

dizionario["a"] = "alto"
lista[0] = "alto"

print(dizionario["a"])
print (lista[0])

for chiave in dizionario: 

    print (f"la chiave {chiave} ha valore {dizionario[chiave]}")
    
#for indice in lista:

    #print (f"l'indice {indice} ha valore {lista[indice]}")

if "a" in dizionario: 
    print("a è presente nel dizionario")


