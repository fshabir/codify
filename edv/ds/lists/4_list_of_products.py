
class ListOfProducts(object):
    def solution1(self, lst):
        res = [1] * len(lst)
        for i, elm1 in enumerate(lst):
            for j, elm2 in enumerate(lst):
                if i != j:
                    res[i] *= elm2
        return res

    def solution2(self, lst):
        product = 1
        zeros = []
        res = [0] * len(lst)
        for i, elm in enumerate(lst):
            if elm != 0:
                product *= elm
            else:
                zeros.append(i)
                if len(zeros) == 2:
                    return res

        if len(zeros) == 1:
            res[zeros[0]] = product
        else:
            for i, elm in enumerate(lst):
                res[i] = product // elm
        return res

    def solution3(self, lst):
        left = 1
        res = []
        for i, elm in enumerate(lst):
            product = 1
            for j, _ in enumerate(lst[i+1:]):
                product *= _
            res.append(product * left)
            left *= elm
        return res

    def solution4(self, lst):
        left = 1
        products = []
        for elm in lst:
            products.append(left)
            left *= elm

        right = 1
        for i in range(len(lst) - 1, -1, -1):
            products[i] *= right
            right *= lst[i]

        return products

arr = [1,2,3,4]
arr = [0,2,0,4]
print(f"Input => {arr}")
inst = ListOfProducts()

print(f"Solution 1 => {inst.solution1(arr)}")
print(f"Solution 2 => {inst.solution2(arr)}")
print(f"Solution 3 => {inst.solution3(arr)}")
print(f"Solution 4 => {inst.solution4(arr)}")