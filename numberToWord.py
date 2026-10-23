def numberToWord(n):
    once = {
             0: "", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
            6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
            11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
            15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen",
            19: "nineteen"
        }
    tens = {
            20: "twenty", 30: "thirty", 40: "forty", 50: "fifty",
            60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"
        }
    if n == 0 :
        return "Zero"
    if n<20:
        return once[n]
    if n<100:
        t = (n//10)*10
        u = (n%10)
        if u == 0 :
            return tens[t]
        return tens[t] + " "+once[u]
    h = n// 100
    rest = n %100

    if rest == 0:
        return once[h]+" hundread"
    else:
        return once[h]+" hundread" +" "+ numberToWord(rest)

n  = 999
print(numberToWord(n))
    
    