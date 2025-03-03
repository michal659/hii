# list, tuple, set, dict

# list
my_list = [6, 2, 8, "abc", True, 5]
my_list.append(10)  # add to end
my_list.insert(2, "new")  # add to index 2
my_list.pop(3)  # delete by index
my_list.remove("abc")  # delete by value
# my_list.sort()
# print(my_list)

names = ["yael", "eti", "riki", "michalb", "margalit"]
# names.sort()  # sort in-place
# print(names)

names.sort(key=len)
print(names)


def last(st):
    return st[-1]


names.sort(key=last)
print(names)


help(names.sort)
