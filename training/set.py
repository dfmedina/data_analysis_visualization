
class Set(object):
    def __init__(self, iterable=()):
        self.elements = []
        for item in iterable:
            self.add(item)

    def add(self, item):
        if item not in self.elements:
            self.elements.append(item)

    def remove(self, elem):
        self.elements.remove(elem)

    def diff(self, set2):
        diff = []
        for elem in set2:
            if elem not in self.elements:
                diff.append(elem)
        return diff

    def inter(self, set2):
        inter = []
        for elem in set2:
            if elem in self.elements:
                inter.append(elem)
        return inter

    def symm_diff(self, set2):
        symm_diff = []
        for elem in set2:
            if elem not in self.elements:
                symm_diff.append(elem)
        for l_elem in self.elements:
            if l_elem not in set2:
                symm_diff.append(l_elem)
        return symm_diff

    def cart_prod(self, set2):
        cart = []
        for elem in set2:
            for l_elem in self.elements:
                cart.append((elem, l_elem))
        return cart

    def power_set(self, i_set):
        if not i_set:
            return [[]]
        with_first_elem = [[i_set[0]] + rest for rest in self.power_set(i_set[1:])]
        without_first_elem = self.power_set(i_set[1:])
        return with_first_elem + without_first_elem

if __name__ == '__main__':
    #set_instance = Set([1, 2, 3, 2, 3, 4, 4, 4])
    #set_instance.add(5)
    #set_instance.remove(2)
    #print set_instance.elements
    #print set_instance.diff([1, 2, 3, 4, 5, 6])
    #print set_instance.inter([1, 2, 3, 4, 5, 6])
    set_instance = Set([2, 4, 6, 8, 10, 12, 14, 16])
    #print set_instance.symm_diff([1, 4, 9, 16, 25])
    #print set_instance.cart_prod([1, 4, 9, 16, 25])
    #print set_instance.power_set()
    print set_instance.power_set([1, 2])
