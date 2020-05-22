# def sol(x):
#     s = ""
#     m = "-"

#     x = list(map(str, str(x)))
#     for char in x:
#         if char == '-':
#             x.remove(char)
#             x = x[::-1]
#             x.insert(0,m)

            
#         elif x[len(x)-1] == "0":
#             x.remove(x[len(x)-1])
#             x = x[::-1]
        
#         else:
#             x = x[::-1]
            
#         for ele in x:
#             s += ele
#         return s


# x = -123
# print(sol(x))

def sol(s):
    dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    sum = 0

        
    for i in range(len(s)):
        if s[i-1] != s[i]:
            if dict[s[i-1]] < dict[s[i]]:
                sum = sum + dict[s[i-1]] + dict[s[i]]
            elif dict[s[i-1]] > dict[s[i]]:
                sum = sum + dict[s[i]] - dict[s[i-1]]
            return abs(sum)
        else:
            sum = sum + dict[s[i]]
    return sum
            
     
s = 'IX'
print(sol(s))