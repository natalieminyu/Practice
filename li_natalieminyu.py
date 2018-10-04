import math

def main():

    num = int(input("Enter the range you would like to test: 0 -? "))
    new_num = num + 1
    sieve = [0] * new_num #creates a list of n+1 values

    for i in range(new_num):
        sieve[i] = "P"

    sieve[0] = "N" # 0 and 1 are not prime numbers
    sieve[1] = "N"
    
    for i in range(2, int(math.sqrt(num)) ): # stops at integer larger than the square root because all multiples afterwards would have been marked
        a = i * 2 #start at the first multiple of i after i 
        while a < new_num:
            if i == "N":
                continue
            sieve[a] = "N" # set an index in the sieve list to "N" for the multiples
            a += i #change a to point to the next multiple of i
  
    counter = 0
    for i in range (len(sieve)):
        if sieve[i] == "P":
            print(format(str(i), ">2s"), end = " ")
            counter += 1

        if counter == 10:
            print()
            counter = 0

            

main ()
