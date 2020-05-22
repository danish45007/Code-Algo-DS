# """Star Printing..."""
# n = int(input("Enter the number of rows:"))
#
# for row in range(n):
#     for col in range(row+1):
#         print("*",end=" ")
#     print()
#
# """Triangle printing"""
# n = int(input("Enter the number of rows:"))
# for i in range(0,n):
#     for j in range(0,n-i-1):
#         print(end=" ")
#     for j in range(0,i+1):
#         print("*",end="")
#     print()

# num = 123
# num = str(num)
# print(num[::-1])

# s = "danish"
# sub_s = "nish"
#
# def sub_finder(s,sub_s):
#     for i in range(len(s)):
#         if s[i:i+len(sub_s)] == sub_s:
#             return "Yes"
#         else:
#             return "No"
#
# a = sub_finder("danish","dan")
# print(a)

# s = "Sorting1234"
# k=sorted(s,key=lambda x:(x.isdigit(),x.isupper(),x.islower(),x.isdigit() and int(x) % 2==0,x))
# j=str(k).strip("[],''")
# j=j.replace(",","")
# j=j.replace("'","")
# j=j.replace(" ","")
# print(k)


#S="GATTACA"
#GATTA
#ATTA
#TTAC
#TACA

# def k_mer(String,n):
#     for i in range(len(String)):
#         String = String[i:i+4]
#
#
#
#
#
# if __name__ == "__main__":
#     String = "GATTACA"
#     n = 4
#     print(k_mer(String,n))


# def fib(n):
#     if n == 1:
#         return 0
#     if n == 2:
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)
# print(fib(9))

# def fact(n):
#     l = []
#     r = 1
#     for i in range(1,n+1,1):
#         l.append(i)
#     for c in l:
#         r = r*c
#     return r
# print(fact(5))
#

# string1 = "HEART"
# string2 = "EART"
# string1 = sorted(string1)
# string2 = sorted(string2)
# if string1 == string2:
#     print("Yes")
# else:
#     print("No")

n = 4
for i in range(2,n*10,10):
    print(i)