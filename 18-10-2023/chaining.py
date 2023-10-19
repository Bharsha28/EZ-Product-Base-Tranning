# input:12 23 45 42 54 53 65 65 75
# output:[[], [], [12, 42], [23, 53], [54], [45, 65, 65, 75], [], [], []]
# search=list(map(int,input().split()))
# l=[[] for i in range(len(search))]
# for i in range(len(search)):
#     has=search[i]%10
#     l[has].append(search[i])
# print(l)
# '''def hash_fun(value):
#     return value%10
# def main():
#     s=[12,23,45,42,54,53,65,65,75]
#     n=9
#     l=[[] for i in range(len(s))]
#     for i in s:
#         has=hash_fun(i)
#         l[has].append(i)
# main()'''
#     
#

def hash_function(value):
    return value%10
def main():
    search_keys = [12,23,45,43,42,54,53,65,75,67,87]
    n = 11
    hash_table = [[] for i in range(n)]
    for value in search_keys:
        hash_value = hash_function(value)
        hash_table[hash_value].append(value)
    print(hash_table)
main()
