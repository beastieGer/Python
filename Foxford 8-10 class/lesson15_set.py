"""
Перебор всех подмножеств
"""

# def generate(n, prefix):
#     if n == 0:
#         print(prefix)
#     else:
#         generate(n-1, prefix + "0")
#         generate(n-1, prefix + "1")
#
#
# generate(5, "")


"""
Перебор всех k-элементных подмножеств
"""

# def generate(n, k, prefix):
#     if n == 0:
#         print(prefix)
#     else:
#         if k < n:
#             generate(n-1, k, prefix + "0")
#         if k > 0:
#             generate(n-1, k-1, prefix + "1")
#
#
# generate(4, 2, "")


"""
Построение всех возрастающих последовательностей длины k
"""

# def generate(n, k, prefix):
#     if k == 0:
#         print(prefix)
#     else:
#         if len(prefix) == 0:
#             next = 1
#         else:
#             next = prefix[-1] + 1
#         while next + k - 1 <= n:
#             generate(n, k-1, prefix + [next])
#             next += 1
#
# sp = []
# generate(4, 2, sp)

"""
Перебор всех перестановок
"""


def generate(n, prefix):
    if len(prefix) == n:
        print(prefix)
    else:
        for next in range(1, n+1):
            if next not in prefix:
                generate(n, prefix + [next])


sp = []
generate(3, sp)
