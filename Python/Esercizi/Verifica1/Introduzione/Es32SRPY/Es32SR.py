#list comprension
#p chiedi una subnet mask che va da 1 a 31 e restituisci la annotazione decimale puntata passando oer ul binario

def main():

    num = int (input("insert a number from 1 to 31: /"))

    ip_address = "192.168.1.1"

    if (num > 31):

        print ("no I said from 1 to 31")

    else:



        subbin = ("1"*num) + ("0"* (32 - num))

        group1 = subbin[0:8]

        group2 = subbin[8:16]

        group3 = subbin[16:24]

        group4 = subbin[24:32]

        group1=int(group1,2)

        group2=int(group2,2)

        group3=int(group3,2)

        group4=int(group4,2)

        ip=f"{group1}.{group2}.{group3}.{group4}"
        
        print(ip)



        print (subbin)



    

        

if __name__ == "__main__":
    main()

