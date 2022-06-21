def length(ll, res=None):
    res = [] if res is None else res
    res.append(len(ll))
    for i in ll:
        if isinstance(i, list):
            length(i, res)
    return sum(res)


my_list = [1, 2, 3, [1, 2, [1, 2], [4, [5, [6, [4]]], [3, 1]]]]
print(length(my_list))

#изначально рассчитывала на следующий вариант, но он не работает корректно. Не смогла определить в чем ошибка,
#поэтому в итоге сделала через еще один список

# def length_sum(ll, res=0):
#     res += len(ll)
#     for i in ll:
#         if isinstance(i, list):
#             length_sum(i, res)
#     return res
