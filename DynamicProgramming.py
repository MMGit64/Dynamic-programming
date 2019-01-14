def module_Sum(arr,n,m):

    if (n > m):
        return True             #Ensures that list of number or added numbers within 'n' are larger than 'm', otherwise 'm' would be out of range for division.

    DP = [False for i in range(m)]      #Initalizes an array as false

    for i in range(n):
        if (DP[0]):
            return True                             # If 'n' list of number or numbers can be divided by m, the program is done

        temp = [False for i in range(m)]            # 'temp' is used to deal with any new additional figures added to the set if DP[J] was true beforehand

        for j in range(m):
            if DP[j] == True:
                if DP [(j + arr[i]) % m] == False:
                   temp[(j + arr[i]) % m] = True

        for j in range(m):
            if (temp[j]):
                DP[j] = True

        #DP[arr[i] % m] = True        
    return DP[0]

arr = [6,9,12, 24]
n = len(arr)
m = 3

if (module_Sum(arr,n,m)):
   print("Yes, m is divisible.")

else:
    print("No, m is not divisible")
