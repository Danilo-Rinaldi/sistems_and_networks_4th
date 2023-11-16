#list comprension
#p 73 n 21

def complete8bit(strbin):
    b = strbin[2:]
    l = len(b)
    return "0"*(8 - l) + b

def main():

    ip_adress = input("give me an ip address: ")

    ip_adress = "192.168.1.1"

    groups = ip_adress.split(".") #I take ip_address and I split it where there is the dot and I obtain a list of lists of strings

    groups = [int (group) for group in groups]# I traduce strings in integer



#    groups = [bin(group)[2:].zfill(8) for group in groups]#I traduce it in binary String and I add the necessary 0

    groups = [bin(group)for group in groups]


    #print (groups)

    print(complete8bit(groups[3]))

    groups_strbin = [complete8bit(group) for group in groups]

    print (groups_strbin)

    #join is the opposite of split 

    print (".".join(groups_strbin))


if __name__ == "__main__":
    main()

