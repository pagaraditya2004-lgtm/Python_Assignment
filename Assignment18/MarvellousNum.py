def ChkPrime(Arr):
    
    PrimeArr = []

    for element in Arr:

        isPrime = True

        for i in range(2,element):
            if element % i == 0:
                isPrime = False
                break
        
        if isPrime == True and element > 1:
            PrimeArr.append(element)

    return PrimeArr


    