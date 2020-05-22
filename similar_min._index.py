# l1 = ["Shogun","Tapioca Express","Burger King","KFC"]
# l2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]

l1 = ["danish", "aditya", "akhil"]
l2 = ["akhil", "akhil", "danish", "dd"]

def sol(l1,l2):
    hash_map = dict()
    for i,s in enumerate(l1):
        hash_map[s] = i
    min_sum = 2000
    res = []

    for i,s in enumerate(l2):
        if s in hash_map:
            temp = i + hash_map[s]

            if temp < min_sum:
                res.clear()
                res.append(s)
                min_sum = temp
            elif temp == min_sum:
                res.append(s)
    return res

print(sol(l1,l2))
