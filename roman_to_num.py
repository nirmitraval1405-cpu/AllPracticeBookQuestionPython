def romantonum(x):
    num=[1,4,5,9,10,40,50,90,100,400,500,900,1000]
    roman=["I","IV","V","IX","X","XL","L","XC","C","CD","D","CM","M"]
    roman_num=""
    i=12
    while x!=0:
        if num[i]<=x:
            roman_num+=roman[i]
            x=x-num[i]
        else:
            i-=1
    return roman_num

def numtoroman(a):
    values={
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000,
    }
    n=0

    for i in range(len(a)):
        if i+1<len(a) and values[a[i]]<values[a[i+1]]:
            n=n-values[a[i]]
        else:
            n=n+values[a[i]]
    return n