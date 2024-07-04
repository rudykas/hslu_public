

# def max_of_three(a, b, c):
#     if a >= b:
#         if a >= c:
#             return a
#         else:
#             return c
#     elif c >= b:
#         return c
#     return b

def max_of_two(a,b):
    if a > b: return a
    return b

print(max_of_two(11,12))

# def max_of_three(a,b,c):
#     if a > max_of_two(b, c):
#         return a
#     return max_of_two(b, c)

def max_of_three(a,b,c):
    return max_of_two(a,max_of_two(b,c))

print(max_of_three(10, 12, 11))
