#make a program that tells how many perfect squares there are in range 0 to 200

def main():

    find = 0

    for i in range (0, 200):
        for k in range (0, i):
            if i == k * k:
                find = find + 1
    
    print(f"there are {find} perfect squares from 0 to 200")
    


if __name__ == "__main__":
    main()