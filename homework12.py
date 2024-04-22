
def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(1, 2, 3)
print_params(1, 2)
print_params("bool")
print_params(b=25)
print_params(c=[1,2,3])

values_lis = [1, "List", True]
values_dict = {"a": 1, "b": 'cool', "c": False}
print_params(*values_lis)
print_params(**values_dict)

values_list_2 = [2, "list"]
print_params(*values_list_2, 42)