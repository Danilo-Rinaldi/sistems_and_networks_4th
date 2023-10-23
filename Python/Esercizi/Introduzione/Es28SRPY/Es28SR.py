#list comprension
#p 73 n 18

import math

def main():

    max = 200

    #power = [i * i for i in range(int (math.sqrt(max)) + 1)] correct

    power_1 = [i**2 for i in range(int (math.sqrt(max)) + 1) if (i % 2 != 0) and (i**2 < max)]

    print(power_1)


if __name__ == "__main__":
    main()

